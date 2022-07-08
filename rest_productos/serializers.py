from rest_framework.serializers import ModelSerializer
from core.models import Productos

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id','nombre','precio','stock','descripcions']

