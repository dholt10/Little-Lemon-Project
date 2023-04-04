from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.get(title="Red Velvet", price=12, inventory=4)
        self.assertEqual(item, "IceCream : 12")