from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from item.models import Item, Warehouse, Position, Category, Units
from item.serializers import ItemsSerializer


class ItemsAPITestCase(APITestCase):
    def test_get(self):
        wh = Warehouse.objects.create(title='Test Store')
        pos = Position.objects.create(title='Test Position')
        cat = Category.objects.create(title='Test Category')
        units = Units.objects.create(title='Test Units')
        item_1 = Item.objects.create(title='Test item 1', cat=cat, wh=wh, pos=pos, units=units)
        item_2 = Item.objects.create(title='Test item 2', cat=cat, wh=wh, pos=pos, units=units)
        url = reverse('item-list')

        response = self.client.get(url)
        serializer_data = ItemsSerializer([item_1, item_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        print (serializer_data)