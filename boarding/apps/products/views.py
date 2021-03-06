import json
from django.http  import JsonResponse

from apps.user.models import User
from apps.products.models import Products
from apps.products.serializers import ProductsSerializer, ProdcutFundingSerializer

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

# from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ProductApplyAPI(APIView):

    def post(self, request, product_id):

        user = self.request.user
        product = Products.objects.get(pk=product_id)

        product.applicants.add(user.id)
        data = {
            'message' : f"{user}님 신청 완료 되었습니다."
        }

        return Response(data)
        

class ProductsViewSet(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    # filter_backends = [DjangoFilterBackend] # DjangoFilterBackend 로 필터링 백엔드 등록
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['title', 'description']
    filterset_fields = ['title', 'description'] # 필터링할 필드 리스트 지정

    ordering_fields = ['created_at', 'total_funding'] # ?ordering= -> 정렬을 허용할 필드의 화이트 리스트. 미지정 시에 serializer_class에 지정된 필드들.
    ordering = ['created_at', 'total_funding'] # 디폴트 정렬을 지정

    

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

    def post(self, request, format=None):
        """
        상품을 등록합니다.
        """
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

        
        
