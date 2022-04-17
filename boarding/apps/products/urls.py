from django.urls import path
from apps.products.views import ProductAPI, FundingAPI, ProductDetailAPI


urlpatterns = [
    path('/products', ProductAPI.as_view()),
    path('/product/<int:product_id>', ProductDetailAPI.as_view()),
    path('/funding/<int:product_id>', FundingAPI.as_view())
]