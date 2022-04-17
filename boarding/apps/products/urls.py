from django.urls import path
from apps.products.views import ProductAPI, FundingAPI


urlpatterns = [
    path('/products', ProductAPI.as_view()),
    path('/funding/<int:product_id>', FundingAPI.as_view())
]