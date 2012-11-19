#!/usr/bin/env python
import os
from distutils.core import setup
app_name = "adminautocomplete"

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)
 
for dirpath, dirnames, filenames in os.walk(app_name):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[len(app_name)+1:] # Strip "app_name/" or "app_name\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

setup(
    name = "django",
    version = '0.3',
    install_requires = [],
    author = "Tim Babych",
    author_email = "tim.babych@gmail.com",
    description = "Mixin for turning foreignKey fields into autocomplete lookups.",
    keywords = "django, admin, autocomplete",
    url = "https://github.com/artscoop/django-admin-autocomplete",
    package_dir = {app_name:app_name},
    packages = packages,
    package_data={app_name: data_files},
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
