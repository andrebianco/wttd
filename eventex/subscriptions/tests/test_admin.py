from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin
from unittest.mock import Mock


class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name='André Bianco',
                                   cpf='12345678901',
                                   email='abianco.allegro@gmail.com',
                                   phone='11-11111-1111')
        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

    def test_has_action(self):
        """Action mark_as paid should be installed."""
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        """It should mark all selected subscriptions as paid."""
        self.call_action()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_message(self):
        """It should send a message to the user."""
        mock = self.call_action()
        mock.assert_called_once_with(None, '1 inscrição foi marcado como paga.')

    def call_action(self):
        queryset = Subscription.objects.all()

        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock

        self.model_admin.mark_as_paid(None, queryset)

        SubscriptionModelAdmin.message_user = old_message_user

        return mock









