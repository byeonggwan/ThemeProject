from rest_framework import serializers
from .models import Big, Middle, Stock, BigComments, MiddleComments, StockComments


class BigCommentsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    body = serializers.CharField(required=True, max_length=200)
    located_at = serializers.SlugRelatedField(slug_field='title', queryset=Big.objects.all())
    
    class Meta:
        model = BigComments
        fields = '__all__'

class MiddleCommentsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    body = serializers.CharField(required=True, max_length=200)
    located_at = serializers.SlugRelatedField(slug_field='title', queryset=Middle.objects.all())

    class Meta:
        model = MiddleComments
        fields = '__all__'

class StockCommentsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    body = serializers.CharField(required=True, max_length=200)
    located_at = serializers.SlugRelatedField(slug_field='title', queryset=Stock.objects.all())

    class Meta:
        model = StockComments
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    middle_theme = serializers.SlugRelatedField(many=True, slug_field='title', queryset=Middle.objects.all())
    comments = StockCommentsSerializer(many=True, read_only=True)
    hot = serializers.BooleanField(read_only=True)
    memory = serializers.BooleanField(read_only=True)

    class Meta:
        model = Stock
        fields = ('id', 'title', 'middle_theme', 'comments', 'hot', 'memory')

class MiddleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    big_theme = serializers.SlugRelatedField(slug_field='title', queryset=Big.objects.all(), default='f')
    stock = StockSerializer(many=True, read_only=True)
    comments = MiddleCommentsSerializer(many=True, read_only=True)
    hot = serializers.BooleanField(read_only=True)
    memory = serializers.BooleanField(read_only=True)

    class Meta:
        model = Middle
        fields = ('id', 'title', 'big_theme', 'stock', 'comments', 'hot', 'memory')

class BigSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    middles = MiddleSerializer(many=True, read_only=True)
    comments = BigCommentsSerializer(many=True, read_only=True)
    hot = serializers.BooleanField(read_only=True)
    memory = serializers.BooleanField(read_only=True)

    class Meta:
        model = Big
        fields = '__all__'

