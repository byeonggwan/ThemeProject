from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import url

urlpatterns = [
    path('big/', views.BigList.as_view()),
    path('big/<int:id>/', views.BigDetail.as_view()),
    path('middle/', views.MiddleList.as_view()),
    path('middle/<int:id>/', views.MiddleDetail.as_view()),
    path('stock/', views.StockList.as_view()),
    path('stock/<int:id>/', views.StockDetail.as_view()),
]
