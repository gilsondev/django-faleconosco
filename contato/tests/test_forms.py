# -*- coding: utf8 -*-

from django.test import TestCase

from contato.forms import ContatoForm


class ContatoFormTest(TestCase):
    """Testes unitários do formulário
    de contato
    """

    def test_contato_sem_nome(self):
        """O email e enviado sem nome?"""
        contato = ContatoForm({
            'nome': '',
            'email': 'email@amail.com',
            'assunto': 'Assunto de Teste',
            'mensagem': 'Aqui fica a mensagem do email'
        })

        self.assertFalse(contato.is_valid())

    def test_contato_sem_email(self):
        """O email e enviado sem email?"""
        contato = ContatoForm({
            'nome': 'Fulano Castro',
            'email': '',
            'assunto': 'Assunto de Teste',
            'mensagem': 'Aqui fica a mensagem do email'
        })

        self.assertFalse(contato.is_valid())

    def test_contato_com_email_invalido(self):
        """O email e enviado com email invalido?"""
        contato = ContatoForm({
            'nome': 'Fulano Castro',
            'email': 'email.amailcom',
            'assunto': 'Assunto de Teste',
            'mensagem': 'Aqui fica a mensagem do email'
        })

        self.assertFalse(contato.is_valid())

    def test_contato_sem_assunto(self):
        """O email e enviado sem assunto?"""
        contato = ContatoForm({
            'nome': 'Fulano Castro',
            'email': 'email@amail.com',
            'assunto': '',
            'mensagem': 'Aqui fica a mensagem do email'
        })

        self.assertFalse(contato.is_valid())

    def test_contato_sem_mensagem(self):
        """O email e enviado sem mensagem?"""
        contato = ContatoForm({
            'nome': 'Fulano Castro',
            'email': 'email@amail.com',
            'assunto': 'Assunto de Teste',
            'mensagem': ''
        })

        self.assertFalse(contato.is_valid())