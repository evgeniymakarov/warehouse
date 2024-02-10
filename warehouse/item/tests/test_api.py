from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from item.models import Item, Warehouse, Position, Category, Units
from item.serializers import ItemsSerializer


class ItemsAPITestCase(APITestCase):
    def setUp(self):
        wh = Warehouse.objects.create(title='Test Store')
        pos = Position.objects.create(title='Test Position')
        cat = Category.objects.create(title='Test Category')
        units = Units.objects.create(title='Test Units')
        self.item_1 = Item.objects.create(title='Test item 1', cat=cat, wh=wh, pos=pos, units=units, amount=10)
        self.item_2 = Item.objects.create(title='Test item 223', cat=cat, wh=wh, pos=pos, units=units, amount=55)
        self.item_3 = Item.objects.create(title='Test item 3', cat=cat, wh=wh, pos=pos, units=units, amount=223)
        self.item_4 = Item.objects.create(title='Test item 1000', cat=cat, wh=wh, pos=pos, units=units, amount=55)

    def test_get(self):
        url = reverse('item-list')
        response = self.client.get(url)
        serializer_data = ItemsSerializer([self.item_1, self.item_2, self.item_3, self.item_4], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        url = reverse('item-list')
        response = self.client.get(url, data={'amount': 55})
        serializer_data = ItemsSerializer([self.item_2, self.item_4], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('item-list')
        response = self.client.get(url, data={'search': 223})
        serializer_data = ItemsSerializer([self.item_2, self.item_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_ordering(self):
        url = reverse('item-list')
        response = self.client.get(url, data={'ordering': '-id', 'amount': '55'})
        serializer_data = ItemsSerializer([self.item_4, self.item_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
