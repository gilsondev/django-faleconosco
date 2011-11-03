# -*- coding: utf8 -*-

from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('contato.views',
    # Form
    url(r'^contato/$', 'form', name='contato_form'),

    # Success
    url(r'^contato/sucesso/$', direct_to_template,
        {'template': 'contato/contato_success.html'}, name='contato_success'),
)
