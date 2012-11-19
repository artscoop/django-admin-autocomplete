#!/usr/bin/env python

from distutils.core import setup

setup(
    name = "Django Autocomplete Mixin",
    version = '0.3',
    install_requires = ['django>=1.0'],
    author = "Tim Babych",
    author_email = "tim.babych@gmail.com",
    description = "Mixin for turning foreignKey fields into autocomplete lookups.",
    keywords = "django, admin, autocomplete",
    url = "https://github.com/artscoop/django-admin-autocomplete",
    py_modules=['django_admin_autocomplete.admin_autocomplete_mixin'],
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
