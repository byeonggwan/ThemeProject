from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls import url

router = DefaultRouter()
router.register(r'big', views.BigViewSet)
router.register(r'middle', views.MiddleViewSet)
router.register(r'stock', views.StockViewSet)
router.register(r'bigcomments', views.BigCommentsViewSet)
router.register(r'middlecomments', views.MiddleCommentsViewSet)
router.register(r'stockcomments', views.StockCommentsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]