#!/usr/bin/env python
import os
from distutils.core import setup
app_name = "django_admin_autocomplete"

setup(
    name = app_name,
    version = '0.3',
    install_requires = [],
    author = "Tim Babych",
    author_email = "tim.babych@gmail.com",
    description = "Mixin for turning foreignKey fields into autocomplete lookups.",
    keywords = "django, admin, autocomplete",
    url = "https://github.com/artscoop/django-admin-autocomplete",
    package_dir = {app_name:app_name},
    packages = [app_name],
    package_data = {app_name:['static/*']},
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
