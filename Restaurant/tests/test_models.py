from django.test import TestCase
from Restaurant.models import Menu


class MenuTest(TestCase):
    """Performing test for the Manu model."""

    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=80, inventory=100)
        self.assertEqual(str(item),'IceCream : 80' )
