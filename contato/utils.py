# -*- coding: utf8 -*-

from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def enviar_email(from_email, to, name, subject, template, tags):
    """Envia o email com o email do destinatário
    assunto e mensagem, renderizando-o usando a partir
    de um arquivo separado
    """
    if from_email is None:
        raise ValueError('Insira o email de origem.')
    if to is None:
        raise ValueError('Insira o email de destino.')
    if name is None:
        raise ValueError(u'Insira o nome do responsável pelo email.')
    if subject is None:
        raise ValueError('Email sem Assunto. Insira corretamente.')
    if template is None:
        raise ValueError(u'Template não encontrado.')
    if tags is None:
        raise ValueError(u"""
        Conteúdo da Mensagem não encontrado. Crie um dicionário com a chave e o
         valor contendo o conteúdo necessário""")

    # Gera a mensagem
    message = render_to_string(template, tags)

    # Envia a mensagem
    send_mail(subject=settings.EMAIL_SUBJECT_PREFIX + " " + subject,
        message=message,
        from_email=from_email,
        recipient_list=[to])
