from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls import url

urlpatterns = [
    path('bigs/', views.BigList.as_view()),
    path('bigs/<int:big_id>/', views.BigDetail.as_view()),
    path('bigs/<int:big_id>/comments/', views.BigCommentList.as_view()),
    path('bigs/<int:big_id>/middles/', views.MiddleList.as_view()),
    path('bigs/<int:big_id>/middles/<int:middle_id>/', views.MiddleDetail.as_view()),
    path('bigs/<int:big_id>/middles/<int:middle_id>/comments', views.MiddleCommentList.as_view()),
    path('bigs/<int:big_id>/middles/<int:middle_id>/stocks/', views.StockList.as_view()),
    path('bigs/<int:big_id>/middles/<int:middle_id>/stocks/<int:stock_id>/', views.StockDetail.as_view()),
    path('bigs/<int:big_id>/middles/<int:middle_id>/stocks/<int:stock_id>/comments', views.StockCommentList.as_view()),
]
