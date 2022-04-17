from rest_framework import serializers

from .models import Products
from apps.user.serializers import FundingUserSerializer


class ProductsSerializer(serializers.ModelSerializer):

    author_user = FundingUserSerializer(read_only=True)

    class Meta:
        model = Products
        fields = '__all__'
        # fields = ('id', 'title', 'author', 'description', 'goal_price', 'goal_percent')

class ProdcutFundingSerializer(serializers.Serializer):

    once_funding = serializers.IntegerField()
    total_funding = serializers.IntegerField()
    goal_price = serializers.IntegerField()
    goal_percent = serializers.IntegerField()
    
    class Meta:
        models = Products
        field  = ('once_funding', 'total_funding', 'goal_price', 'goal_percent')
