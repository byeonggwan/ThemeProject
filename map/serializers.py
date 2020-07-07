from rest_framework import serializers
from .models import Big, Middle, Stock, BigComments, MiddleComments, StockComments

class BigSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    
    class Meta:
        model = Big
        fields = '__all__'

class MiddleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)

    class Meta:
        model = Middle
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    
    class Meta:
        model = Stock
        fields = '__all__'

class BigCommentsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    body = serializers.CharField(required=True, max_length=200)
    located_at = serializers.CharField(required=True, max_length=100)

    class Meta:
        model = BigComments
        fields = '__all__'

class MiddleCommentsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    body = serializers.CharField(required=True, max_length=200)
    located_at = serializers.CharField(required=True, max_length=100)

    class Meta:
        model = MiddleComments
        fields = '__all__'

class StockCommentsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    body = serializers.CharField(required=True, max_length=200)
    located_at = serializers.CharField(required=True, max_length=100)

    class Meta:
        model = StockComments
        fields = '__all__'