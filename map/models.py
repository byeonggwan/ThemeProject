from django.db import models

# Create your models here.


class Big(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Middle(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    big_theme = models.ForeignKey(Big, on_delete=models.CASCADE)


class Stock(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    middle_theme = models.ManyToManyField(Middle, blank=True)


class BigComments(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    located_at = models.ForeignKey(Big, on_delete=models.CASCADE)

class MiddleComments(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    located_at = models.ForeignKey(Middle, on_delete=models.CASCADE)

class StockComments(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    located_at = models.ForeignKey(Stock, on_delete=models.CASCADE)



