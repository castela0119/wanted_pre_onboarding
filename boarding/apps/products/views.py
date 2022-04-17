from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.user.models import User
from apps.products.models import Products
from apps.products.serializers import ProductsSerializer, ProdcutFundingSerializer

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

class FundingAPI(APIView):

    def post(self, request, product_id):
        """
        1회 펀딩금액만큼 펀딩하는 로직입니다.
        """
        product = Products.objects.get(pk=product_id)

        print(f"product 입니다. : {product}")
        # serializser.data
        product.total_funding += product.once_funding

        product.goal_percent = (product.total_funding / product.goal_price) * 100

        product.save()
        product = ProdcutFundingSerializer(product)

        print(f"product 입니다. : {product.data}")


        return Response(product.data)

        
        
