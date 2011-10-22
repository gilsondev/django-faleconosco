# -*- coding: utf8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _


class ContatoForm(forms.Form):
    """Formulário de Contato"""
    nome = forms.CharField(label=_(u'Nome Completo'), max_length=80)
    email = forms.EmailField(label=_(u'E-mail'), max_length=100)
    assunto = forms.CharField(label=_(u'Assunto'), max_length=80)
    mensagem = forms.CharField(label=_(u'Mensagem'),
        widget=forms.Textarea(attrs={'cols': 80}), max_length=200)
