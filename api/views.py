from .models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Details': '/product-detail/<str:pk>/',
        'Create': '/product-create/',
        'Update': '/product-update/<str:pk>/',
        'Delete': '/product-delete/<str:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    seriolizer = ProductSerializer(products, many=True)
    return Response(seriolizer.data)


@api_view(['GET'])
def productDetails(request, pk):
    products = Product.objects.get(id=pk)
    seriolizer = ProductSerializer(products, many=False)
    return Response(seriolizer.data)


@api_view(['POST'])
def productCreate(request):
    seriolizer = ProductSerializer(data=request.data)
    if seriolizer.is_valid():
        seriolizer.save()
    return Response(seriolizer.data)


@api_view(['POST'])
def productUpdate(request, pk):
    product = Product.objects.get(id=pk)
    seriolizer = ProductSerializer(instance=product, data=request.data)
    if seriolizer.is_valid():
        seriolizer.save()
    return Response(seriolizer.data)


@api_view(['DELETE'])
def productDelete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response("Item successifully deleted!")
