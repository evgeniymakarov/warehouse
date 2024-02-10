from django.test import TestCase

from item.models import Warehouse, Position, Category, Units, Item
from item.serializers import ItemsSerializer

'''
проверка работы сериализатора ItemsSerializer
'''
class ItemsSerializerTestCase(TestCase):
    def setUp(self):
        wh = Warehouse.objects.create(title='Test Store')
        pos = Position.objects.create(title='Test Position')
        cat = Category.objects.create(title='Test Category')
        units = Units.objects.create(title='Test Units')
        self.item_1 = Item.objects.create(title='Test item 1', cat=cat, wh=wh, pos=pos, units=units, amount=10)
        self.item_2 = Item.objects.create(title='Test item 2', cat=cat, wh=wh, pos=pos, units=units, amount=55)


    def test_ok(self):
        data = ItemsSerializer([self.item_1, self.item_2], many=True).data
        expected_data = [
            {
                'id': self.item_1.id,
                'title': 'Test item 1',
                'item_photo': None,
                'created_at': self.item_1.created_at.replace(tzinfo=None).isoformat()+'Z',
                'updated_at': self.item_1.updated_at.replace(tzinfo=None).isoformat()+'Z',
                'amount': '10',
                'cat': self.item_1.cat.id,
                'wh': self.item_1.wh.id,
                "pos": self.item_1.pos.id,
                "units": self.item_1.units.id,
            },
            {
                'id': self.item_2.id,
                'title': 'Test item 2',
                'item_photo': None,
                'created_at': self.item_2.created_at.replace(tzinfo=None).isoformat()+'Z',
                'updated_at': self.item_2.updated_at.replace(tzinfo=None).isoformat()+'Z',
                'amount': '55',
                'cat': self.item_2.cat.id,
                'wh': self.item_2.wh.id,
                "pos": self.item_2.pos.id,
                "units": self.item_2.units.id,
            }
        ]
        self.assertEqual(expected_data, data)

