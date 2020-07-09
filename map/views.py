from rest_framework import viewsets, status
from .models import Big, Middle, Stock, BigComments, MiddleComments, StockComments
from .serializers import BigSerializer, MiddleSerializer, StockSerializer, BigCommentsSerializer, MiddleCommentsSerializer, StockCommentsSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer

class BigList(APIView):
    def get(self, request, format=None):
        bigs = Big.objects.all()
        serializer = BigSerializer(bigs, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = BigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MiddleList(APIView):
    def get(self, request, format=None):
        middles = Middle.objects.all()
        serializer = MiddleSerializer(middles, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = MiddleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StockList(APIView):
    def get(self, request, format=None):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BigDetail(APIView):
    def get_object(self, id):
        try:
            return Big.objects.get(id=id)
        except Big.DoesNotExist:
            return Http404
    
    def get(self, request, id, format=None):
        big = self.get_object(id)
        serializer = BigSerializer(big)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        big = self.get_object(id)
        serializer = BigSerializer(big, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        big = self.get_object(id)
        big.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class MiddleDetail(APIView):
    def get_object(self, id):
        try:
            return Middle.objects.get(id=id)
        except Middle.DoesNotExist:
            return Http404
    
    def get(self, request, id, format=None):
        middle = self.get_object(id)
        serializer = MiddleSerializer(middle)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        middle = self.get_object(id)
        serializer = MiddleSerializer(middle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        middle = self.get_object(id)
        middle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StockDetail(APIView):
    def get_object(self, id):
        try:
            return Stock.objects.get(id=id)
        except Stock.DoesNotExist:
            return Http404
    
    def get(self, request, id, format=None):
        stock = self.get_object(id)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        stock = self.get_object(id)
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        stock = self.get_object(id)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def heat(self, request, id):
        theme = self.get_object(id)
        theme.hot = True
        theme.save()
        serializer = BigSerializer(theme)
        return Response(serializer.data)