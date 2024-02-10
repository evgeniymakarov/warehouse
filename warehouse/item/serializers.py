from rest_framework.serializers import ModelSerializer

from item.models import Item


class ItemsSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'