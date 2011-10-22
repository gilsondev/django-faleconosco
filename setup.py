# -*- coding: utf8 -*-

from distutils.core import setup
import os

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('contato'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[13:]
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(name='django-faleconosco',
      version='1.0a',
      description=u'Aplicativo que implementa a seção Fale Conosco do seu Site Portal, etc',
      author='Gilson Filho',
      author_email='contato@gilsondev.com',
      url='https://github.com/gilsondev/django-faleconosco',
      #download_url='http://www.bitbucket.org/ubernostrum/django-registration/get/v0.7.gz',
      package_dir={'contato': 'contato'},
      packages=packages,
      package_data={'contato': data_files},
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
        )
