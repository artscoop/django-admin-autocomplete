#!/usr/bin/env python
import os
from distutils.core import setup
app_name = "admin-autocomplete"

setup(
    name = "django-%s" % app_name,
    version = '0.3',
    install_requires = [],
    author = "Tim Babych",
    author_email = "tim.babych@gmail.com",
    description = "Mixin for turning foreignKey fields into autocomplete lookups.",
    keywords = "django, admin, autocomplete",
    url = "https://github.com/artscoop/django-admin-autocomplete",
    package_dir = {app_name:app_name, 'django_admin_autocomplete':'django_admin_autocomplete'},
    packages = ['django_admin_autocomplete'],
    package_data = {'static':['static/*']},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
