from django.urls import path
from apps.products.views import (
    ProductAPI, 
    FundingAPI, 
    ProductDetailAPI, 
    ProductsViewSet, 
    ProductApplyAPI
    )


urlpatterns = [
    path('/', ProductAPI.as_view()),
    path('/', ProductsViewSet.as_view()),
    path('/<int:product_id>', ProductDetailAPI.as_view()),
    path('/<int:product_id>/apply', ProductApplyAPI.as_view()),
    path('/<int:product_id>/funding', FundingAPI.as_view()),
]