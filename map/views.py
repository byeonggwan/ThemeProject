from rest_framework import viewsets, status
from .models import Big, Middle, Stock, BigComments, MiddleComments, StockComments
from .serializers import BigSerializer, MiddleSerializer, StockSerializer, BigCommentsSerializer, MiddleCommentsSerializer, StockCommentsSerializer, BigsSerializer, MiddlesSerializer, StocksSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer
from django_filters.rest_framework import DjangoFilterBackend


class BigCommentList(APIView):
    def get(self, request, big_id, format=None):
        comments = BigComments.objects.filter(big=big_id)
        serializer = BigCommentsSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, big_id, format=None):
        request.data['big'] = big_id
        serializer = BigCommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MiddleCommentList(APIView):
    def get(self, request, big_id, middle_id, format=None):
        comments = MiddleComments.objects.filter(middle=middle_id)
        serializer = MiddleCommentsSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, big_id, middle_id, format=None):
        request.data['middle'] = middle_id
        serializer = MiddleCommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockCommentList(APIView):
    def get(self, request, big_id, middle_id, stock_id, format=None):
        comments = StockComments.objects.filter(stock=stock_id)
        serializer = StockCommentsSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, big_id, middle_id, stock_id, format=None):
        request.data['stock'] = stock_id
        serializer = StockCommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BigList(generics.ListAPIView):
    model = Big
    serializer_class = BigsSerializer

    def get_queryset(self):
        queryset = Big.objects.all()
        title = self.request.query_params.get('title')
        if title == None:
            return queryset
        queryset = queryset.filter(title=title)
        return queryset

class MiddleList(APIView):
    def get_object(self, big_id):
        try:
            return Middle.objects.filter(big_theme=big_id)
        except Middle.DoesNotExist:
            return Http404
        
    def get(self, request, big_id, format=None):
        middles = self.get_object(big_id)
        serializer = MiddlesSerializer(middles, many=True)
        return Response(serializer.data)
        
    def post(self, request, big_id, format=None):
        request.data['big_theme'] = big_id
        serializer = MiddleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockList(APIView):
    def get_object(self, middle_id):
        try:
            return Stock.objects.filter(middle_theme=middle_id)
        except Stock.DoesNotExist:
            return Http404
    
    def get(self, request, big_id, middle_id, format=None):
        stocks = self.get_object(middle_id)
        serializer = StocksSerializer(stocks, many=True)
        return Response(serializer.data)
        
    def post(self, request, big_id, middle_id, format=None):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BigDetail(APIView):
    def get_object(self, big_id):
        try:
            return Big.objects.get(id=big_id)
        except Big.DoesNotExist:
            return Http404

    def get(self, request, big_id, format=None):
        big = self.get_object(big_id)
        serializer = BigSerializer(big)
        return Response(serializer.data)

    def put(self, request, big_id, format=None):
        big = self.get_object(big_id)
        serializer = BigSerializer(big, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, big_id, format=None):
        big = self.get_object(big_id)
        big.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MiddleDetail(APIView):
    def get_object(self, middle_id):
        try:
            return Middle.objects.get(id=middle_id)
        except Middle.DoesNotExist:
            return Http404
    
    def get(self, request, big_id, middle_id, format=None):
        middle = self.get_object(middle_id)
        serializer = MiddleSerializer(middle)
        return Response(serializer.data)

    def put(self, request, big_id, middle_id, format=None):
        middle = self.get_object(middle_id)
        serializer = MiddleSerializer(middle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, big_id, middle_id, format=None):
        middle = self.get_object(middle_id)
        middle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StockDetail(APIView):
    def get_object(self, stock_id):
        try:
            return Stock.objects.get(id=stock_id)
        except Stock.DoesNotExist:
            return Http404
    
    def get(self, request, big_id, middle_id, stock_id, format=None):
        stock = self.get_object(stock_id)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def put(self, request, big_id, middle_id, stock_id, format=None):
        stock = self.get_object(stock_id)
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, big_id, middle_id, stock_id, format=None):
        stock = self.get_object(stock_id)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BigFindTitle(APIView):
    def get_object(self, big_title):
        try:
            return Big.objects.get(title=big_title)
        except Big.DoesNotExist:
            return Http404
    
    def get(self, request, big_title, format=None):
        print("hsdh")
        big = self.get_object(big_title)
        serializer = BigSerializer(big)
        return Response(serializer.data)

    def put(self, request, big_title, format=None):
        big = self.get_object(big_title)
        serializer = BigSerializer(big, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, big_title, format=None):
        big = self.get_object(big_title)
        big.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)