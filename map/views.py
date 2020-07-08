from rest_framework import viewsets, status
from .models import Big, Middle, Stock, BigComments, MiddleComments, StockComments
from .serializers import BigSerializer, MiddleSerializer, StockSerializer, BigCommentsSerializer, MiddleCommentsSerializer, StockCommentsSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import Http404
# Create your views here.


class BigViewSet(viewsets.ModelViewSet):
    queryset = Big.objects.all()
    serializer_class = BigSerializer

class MiddleViewSet(viewsets.ModelViewSet):
    queryset = Middle.objects.all()
    serializer_class = MiddleSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            print(serializer.data["stock"])
            #안에 종목이 없다면 삭제
            if serializer.data["stock"] == []:
                self.perform_destroy(instance)
            else:
                Response(status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

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


