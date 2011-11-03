# -*- coding: utf8 -*-

from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os

root = os.path.dirname(os.path.abspath(__file__))
os.chdir(root)

VERSION = '1.1a'

# Make data go to the right place.
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

def gen_data_files(*dirs):
    results = []
    for src_dir in dirs:
        for root,dirs,files in os.walk(src_dir):
            results.append((root, map(lambda f:root + "/" + f, files)))
    return results

setup(
    name='django-faleconosco',
    version=VERSION,
    description="Aplicacao responsavel pela secao Fale Conosco de sites, portais, blogs, etc.",
    long_description="Essa aplicacao foi feita para evitar o retrabalho no desenvolvimento da pagina de contato do seu site, blog ou portal..",
    author="Gilson Filho",
    author_email="contato@gilsondev.com",
    url="http://github.com/gilsondev/django-faleconosco",
    license="BSD License",
    platforms=["any"],
    packages=['contato'],
    data_files=gen_data_files(os.path.join('contato', 'templates')),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True,
)
