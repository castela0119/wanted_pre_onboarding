import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.user.models import User
from apps.products.models import Products
from apps.products.serializers import ProductsSerializer, ProdcutFundingSerializer

from django.http  import JsonResponse

# Create your views here.
class ProductAPI(APIView):
    
    def get(self, request, format=None):
        """
        Return a list of all products.
        """
        # usernames = [user.username for user in Products.objects.all()]
        products = Products.objects.all()
        serializser= ProductsSerializer(products, many=True)
        data = {
            "products":products
        }
        return Response(serializser.data)

class ProductDetailAPI(APIView):

    def get(self, request, product_id):

        product = Products.objects.get(pk=product_id)

        product = ProductsSerializer(product)
        
        return Response(product.data)

    
    def post(self, request, product_id):
        """
        특정 Product 내용을 수정합니다.
        단, '목표금액'은 수정할 수 없습니다.
        """
        data = json.loads(request.body)

        product = Products.objects.get(pk=product_id)

        product.title = data.get('title', product.title)
        product.description = data.get('description',  product.description)
        product.end_day = data.get('end_day', product.end_day)

        product.save()

        return JsonResponse({'message': 'SUCCESS'}, status=200)

        


class FundingAPI(APIView):

    def post(self, request, product_id):
        """
        1회 펀딩금액만큼 펀딩하는 로직입니다.
        """
        product = Products.objects.get(pk=product_id)

        # serializser.data
        product.total_funding += product.once_funding

        product.goal_percent = (product.total_funding / product.goal_price) * 100

        product.save()
        product = ProdcutFundingSerializer(product)

        return Response(product.data)

        
        
