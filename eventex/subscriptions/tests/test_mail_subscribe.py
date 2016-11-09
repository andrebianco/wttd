from django.core import mail
from django.test import TestCase

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='André Bianco', cpf='12345678901',
                    email='abianco.allegro@gmail.com', phone='11-11111-1111')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'abianco.allegro@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_description_email_body(self):
        contents =[
            'André Bianco',
            '12345678901',
            'abianco.allegro@gmail.com',
            '11-11111-1111',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)