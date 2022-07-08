from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from core.models import Productos
from rest_productos.serializers import ProductoSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

@csrf_exempt
@api_view(['GET', 'POST'])
def productos(request):
    if request.method == 'GET':
        productos = Productos.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
