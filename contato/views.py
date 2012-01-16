# -*- coding: utf8 -*-

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.conf import settings
from django.core.urlresolvers import reverse

from contato.forms import ContatoForm
from contato.utils import enviar_email


def form(request, template_name='contato/contato_form.html',
    template_email='contato/email.txt', dict={}):
    """Invoca o formulário de contato"""

    contato = ContatoForm(request.POST or None)
    if contato.is_valid():
        nome = contato.data.get('nome')
        email = contato.data.get('email')
        assunto = contato.data.get('assunto')
        mensagem = contato.data.get('mensagem')

        # Construindo o dicionario de dados
        mensagem = {'nome': nome, 'email': email, 'mensagem': mensagem}
        if dict:
            mensagem.update(dict)

        # Enviando o email
        enviar_email(email, settings.DEFAULT_FROM_EMAIL, nome,
            assunto, template_email, mensagem)

        # Mostra mensagem de sucesso
        return redirect(reverse('contato_success'))

    return render_to_response(template_name, {'form': contato},
        context_instance=RequestContext(request))
