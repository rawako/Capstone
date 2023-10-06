from django.test import TestCase
from rest_framework.test import APIClient

from rest_framework import status
from rest_framework.reverse import reverse

from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer


class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        menu1 = Menu.objects.create(title='Item 1', price=10.99, inventory=10)
        menu2 = Menu.objects.create(title='Item 2', price=5.99, inventory=20)
        menu3 = Menu.objects.create(title='Item 3', price=7.99, inventory=200)

    def test_getall(self):
        url = reverse('menu-items')

        res = self.client.get(url)
        all_menu_items = Menu.objects.all()
        serializer = MenuSerializer(all_menu_items, many=True)

        self.assertEqual(serializer.data, res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

