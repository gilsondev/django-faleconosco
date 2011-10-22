# -*- coding: utf8 -*-

from setuptools import setup
import os
 
 
README_FILE = open('README.md')
try:
    LONG_DESCRIPTION = README_FILE.read()
finally:
    README_FILE.close()
 
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'contato', 'templates')
TEMPLATE_DATA = []
for path, dirs, filenames in os.walk(DATA_DIR):
    # Ignore directories that start with '.'
    for i, dir in enumerate(dirs):
        if dir.startswith('.'):
            del dirs[i]
    path = path[len(DATA_DIR) + 1:]
    TEMPLATE_DATA.append(os.path.join('templates', path, '*.*'))
    # Get files starting with '.' too (they are excluded from the *.* glob).
    TEMPLATE_DATA.append(os.path.join('templates', path, '.*'))
 
 
setup(name='django-faleconosco',
      version='1.0a',
      author='Gilson Filho',
      author_email='contato@gilsondev.com',
      description=('Aplicação responsável pela seção Fale Conosco de sites, portais, blogs, etc.'),
      long_description=LONG_DESCRIPTION,
      packages=['contato'],
      package_data={'contato': TEMPLATE_DATA},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules'])
