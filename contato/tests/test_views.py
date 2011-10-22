# -*- coding: utf8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse


class ContatoViewTest(TestCase):
    """Testes unitários da view"""

    def test_form_success(self):
        response = self.client.get(reverse('contato_form'))
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'contato/contato_form.html')
