from rest_framework import serializers
from .models import Big, Middle, Stock, BigComments, MiddleComments, StockComments


class BigCommentsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    body = serializers.CharField(required=True, max_length=200)
    
    class Meta:
        model = BigComments
        fields = '__all__'


class MiddleCommentsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    body = serializers.CharField(required=True, max_length=200)

    class Meta:
        model = MiddleComments
        fields = '__all__'


class StockCommentsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    body = serializers.CharField(required=True, max_length=200)

    class Meta:
        model = StockComments
        fields = '__all__'


class StocksSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    comment_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Stock
        fields = ('id', 'title', 'comment_count', 'is_hot', 'is_old')

    def get_comment_count(self, obj):
        return obj.comments.count()


class StockSerializer(serializers.ModelSerializer):
    comments = StockCommentsSerializer(many=True, read_only=True)


    class Meta:
        model = Stock
        fields = '__all__'


class MiddlesSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    stock_count = serializers.SerializerMethodField(read_only=True)
    comment_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Middle
        fields = ('id', 'title', 'stock_count', 'comment_count', 'is_hot', 'is_old', 'big_theme')

    def get_stock_count(self, obj):
        return obj.stocks.count()

    def get_comment_count(self, obj):
        return obj.comments.count()


class MiddleSerializer(MiddlesSerializer):
    stocks = StockSerializer(many=True, read_only=True)
    comments = BigCommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Middle
        fields = '__all__'


class BigsSerializer(serializers.ModelSerializer): # Big List
    title = serializers.CharField(required=True, max_length=100)
    middle_count = serializers.SerializerMethodField(read_only=True)
    comment_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Big
        fields = ('id', 'title', 'middle_count', 'comment_count', 'is_hot', 'is_old')

    def get_middle_count(self, obj):
        return obj.middles.count()

    def get_comment_count(self, obj):
        return obj.comments.count()


class BigSerializer(BigsSerializer): # Big Detail
    middles = MiddlesSerializer(many=True, read_only=True)
    comments = BigCommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Big
        fields = '__all__'

