django-admin-autocomplete
=========================

Admin mixin providing autocomplete features of ForeignKey fields.

Usage example :

    from django.contrib import admin
    from django_admin_autocomplete import AutocompleteFKMixin

    class ReviewAdmin(AutocompleteFKMixin, admin.ModelAdmin):
        related_search_fields  = {
            # plain lookup
            'manufacturer':('name',),
            # lookup aware of related field
            'line'        :{'search': ('name',), 'related': ('manufacturer',)},
            # lookup aware of two related fields
            'mattress'    :{'search': ('name',), 'related': ('manufacturer','line')},
            'retailer'    :('name',),
            'store'       :{
                # lookup for several fields
                'search': ('name', 'city', 'state__abbr', 'street_address1', 'zip_code'),
                'related': ('retailer',),
                }
            }
