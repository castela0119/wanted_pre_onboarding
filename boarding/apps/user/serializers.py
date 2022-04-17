from rest_framework import serializers

from .models import User

class FundingUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()

    class Meta:
        models = User
        field  = '__all__'