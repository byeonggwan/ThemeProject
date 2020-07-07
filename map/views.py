from rest_framework import viewsets
from .models import Big, Middle, Stock, BigComments, MiddleComments, StockComments
from .serializers import BigSerializer, MiddleSerializer, StockSerializer, BigCommentsSerializer, MiddleCommentsSerializer, StockCommentsSerializer

# Create your views here.

class BigViewSet(viewsets.ModelViewSet):
    queryset = Big.objects.all()
    serializer_class = BigSerializer

class MiddleViewSet(viewsets.ModelViewSet):
    queryset = Middle.objects.all()
    serializer_class = MiddleSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class BigCommentsViewSet(viewsets.ModelViewSet):
    queryset = BigComments.objects.all()
    serializer_class = BigCommentsSerializer

class MiddleCommentsViewSet(viewsets.ModelViewSet):
    queryset = MiddleComments.objects.all()
    serializer_class = MiddleCommentsSerializer

class StockCommentsViewSet(viewsets.ModelViewSet):
    queryset = StockComments.objects.all()
    serializer_class = StockCommentsSerializer


