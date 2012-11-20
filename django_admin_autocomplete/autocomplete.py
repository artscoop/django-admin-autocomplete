# coding: utf-8
# for autocomplete
import operator

from django import forms
from django.db import models
from django.utils.encoding import smart_str
from django.utils.safestring import mark_safe
from django.conf.urls.defaults import patterns
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
from django.template.defaultfilters import striptags


# ModelAdmin Mixin to enable autocompletion
# based and inspired by http://jannisleidel.com/2008/11/autocomplete-form-widget-foreignkey-model-fields/
class AutocompleteFKMixin(object):
    # Add an autocomplete search URL in the ModelAdmin
    def get_urls(self):
        urls = super(AutocompleteFKMixin, self).get_urls()
        search_url = patterns('', (r'^search/$', self.search))
        return search_url + urls
    # Base queryset
    def get_autocomplete_queryset(self, request, field_name):
        """ Returns the basic queryset to filter results for an autocomplete field `field_name`.
        If None is returned - all db objects are used for a queryset. """
        return None
    # Search view
    def search(self, request):
        """ Searches in the fields of the given related model and returns the
        result as a simple string to be used by the jQuery Autocomplete plugin """
        query         = request.GET.get('q', None)
        app_label     = request.GET.get('app_label', None)
        model_name    = request.GET.get('model_name', None)
        search_fields = request.GET.get('search_fields', None)
        field_name    = request.GET.get('field_name', None)
        related_fields = [field[:-3] for field in request.GET
            if field[-3:] == "_pk" and request.GET[field]]

        # remove all garbage and injections
        from django.template.defaultfilters import slugify
        search_fields = [f for f in search_fields.split(',') if f==slugify(f)]

        if search_fields and app_label and model_name and query:
            def construct_search(field_name):
                # use different lookup methods depending on the notation
                if field_name.startswith('^'):
                    return "%s__istartswith" % field_name[1:]
                elif field_name.startswith('='):
                    return "%s__iexact" % field_name[1:]
                elif field_name.startswith('@'):
                    return "%s__search" % field_name[1:]
                else:
                    return "%s__icontains" % field_name

            model = models.get_model(app_label, model_name)
            qs = self.get_autocomplete_queryset(request, field_name)
            if qs is None:
                qs = model._default_manager.all()
            for bit in query.split():
                or_queries = [models.Q(**{construct_search(
                    smart_str(field_name)): smart_str(bit)})
                        for field_name in search_fields]

                other_qs = QuerySet(model)
                other_qs.dup_select_related(qs)
                other_qs = other_qs.filter(reduce(operator.or_, or_queries))
                qs = qs & other_qs
            # filter out by related ids
            qs = qs.filter(**dict([(str(field), request.GET[field+"_pk"]) for field in related_fields]))
            # sort rows directly containing query be the first
            from django.utils.datastructures import SortedDict

            # we do not was to dig into __ relations here. Only first model fields go for smart sorting.
            smartsorted_fields = []
            for field_name in search_fields:
                # add qualifying table
                try:
                    model._meta.get_field_by_name(field_name)
                except:
                    continue
                smartsorted_fields.append(field_name)

            for field_name in smartsorted_fields:
                full_field_name = model._meta.db_table+"."+field_name
                qs = qs.extra(select=SortedDict([
                    ('_%s_match' % field_name,
                        "CASE WHEN lower("+full_field_name+")=lower(%s) THEN 1 ELSE 0 END"),
                    ('_%s_contains' % field_name,
                    # can not put percents here because of http://code.djangoproject.com/ticket/6400
                        "CASE WHEN "+full_field_name+" LIKE %s THEN 1 ELSE 0 END"),
                    ]), select_params = [query, '%'+query+'%'])
            ordering = [ ['-_%s_match' % field_name, '-_%s_contains' % field_name]
                for field_name in smartsorted_fields]
            # flatten list of sorting options
            ordering = sum(ordering, [])
            qs = qs.order_by(*ordering)
            qs = qs[:25]

            # sometimes we want to present suggestions in a special way
            def ajax_str(obj):
                if hasattr(obj, 'ajax_str') and callable(obj.ajax_str):
                    return obj.ajax_str()
                else:
                    return unicode(object)

            data = ''.join([u'%s|%s\n' % (ajax_str(f), f.pk) for f in qs])
            return HttpResponse(data, mimetype='text/plain')
        return HttpResponseNotFound()

    # Change form field for the related search fields
    def formfield_for_dbfield(self, db_field, **kwargs):
        """
        Overrides the default widget for Foreignkey fields if they are
        specified in the related_search_fields class attribute.
        """
        if isinstance(db_field, models.ForeignKey) and hasattr(self, 'related_search_fields') \
                and db_field.name in self.related_search_fields:
            kwargs['widget'] = ForeignKeySearchInput(db_field.rel, self.related_search_fields[db_field.name])
        return super(AutocompleteFKMixin, self).formfield_for_dbfield(db_field, **kwargs)


class ForeignKeySearchInput(forms.TextInput):
    """
    A Widget for displaying ForeignKeys in an autocomplete search input
    instead in a ``select`` box.
    """
    class Media:
        css = {
            'all': ('admin-autocomplete/jquery.autocomplete.css',)
        }
        js = (
            # Breaks our current <script> order. See GoodBed Trac #1061.
            # 'js/jquery.min.js',
            'admin-autocomplete/jquery.autocomplete.js',
        )
    input_type = 'hidden'

    def label_for_value(self, value):
        from django.utils.text import truncate_words
        key = self.rel.get_related_field().name
        obj = self.rel.to._default_manager.get(**{key: value})
        if hasattr(obj, 'ajax_str') and callable(obj.ajax_str):
            obj = obj.ajax_str()
        return truncate_words(obj, 14)

    def __init__(self, rel, search_fields, attrs=None):
        self.rel = rel

        if type(search_fields) == dict:
            # fancy lookup for manufacturer_pk, like_pk etc
            self.search_fields = search_fields['search']
            self.related_fields = search_fields['related']
        else:
            # plain string lookup
            self.search_fields = search_fields
            self.related_fields = None
        super(ForeignKeySearchInput, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if attrs is None:
            attrs = {}
        rendered = super(ForeignKeySearchInput, self).render(name, value, attrs)
        if value:
            label = self.label_for_value(value)
        else:
            label = u''

        if self.related_fields:
            extra_params = ','.join([
                "%s_pk: function(){ return jQuery('#id_%s').val(); }" % (field, field)
                    for field in self.related_fields])
        else:
            extra_params = ''

        # Play nice with Django 1.4
        try:
            admin_media_prefix = settings.ADMIN_MEDIA_PREFIX
        except AttributeError:
            admin_media_prefix = settings.STATIC_URL + "admin/"

        return rendered + mark_safe(u'''
            <style type="text/css" media="screen">
                #lookup_%(name)s {padding-right:20px; background: url(%(admin_media_prefix)simg/selector-search.gif) no-repeat right;}
                #del_%(name)s {display: none;}
            </style>

            <input type="text" id="lookup_%(name)s" value="%(label)s" />
            <a href="#" id="del_%(name)s"> <img src="%(admin_media_prefix)simg/icon_deletelink.gif" /> </a>
            <script type="text/javascript">
                if ($('#lookup_%(name)s').val()) {
                    $('#del_%(name)s').show()
                }
                $('#lookup_%(name)s').ext_autocomplete('../search/', {
                    'minChars': 2, 'cacheLength': 0, 'max':35,
                    'extraParams': {
                        search_fields: '%(search_fields)s',
                        app_label: '%(app_label)s',
                        model_name: '%(model_name)s',
                        field_name: '%(name)s',
                        %(extra_params)s
                    },
                    'formatResult': function(data, text, total) {
                        text = text.replace(/(<([^>]+)>)/ig,""); // Trim tags
                        text = text.replace(/^\s\s*/, '').replace(/\s\s*$/, ''); // Trim spaces
                        return text;
                    }
                }).result(function(event, data, formatted) {
                    if (data) {
                        $('#id_%(name)s').val(data[1]);
                        $('#del_%(name)s').show();
                    }
                });
                $('#del_%(name)s').click(function(ele, event) {
                    $('#id_%(name)s').val('');
                    $('#del_%(name)s').hide();
                    $('#lookup_%(name)s').val('');
                });
        </script>
        ''') % {
            'search_fields': ','.join(self.search_fields),
            'admin_media_prefix': admin_media_prefix,
            'model_name': self.rel.to._meta.module_name,
            'app_label': self.rel.to._meta.app_label,
            'label': striptags(label),
            'name': name,
            'extra_params': extra_params,
        }
