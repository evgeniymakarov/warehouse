from rest_framework import viewsets

from item.models import Item
from item.serializers import ItemsSerializer


# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemsSerializer
