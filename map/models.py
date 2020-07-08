from django.db import models

# Create your models here.


class Big(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    hot = models.BooleanField(default=False)
    memory = models.BooleanField(default=False)

class Middle(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    big_theme = models.ForeignKey(Big, related_name='middles',on_delete=models.CASCADE)
    hot = models.BooleanField(default=False)
    memory = models.BooleanField(default=False)

class Stock(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    middle_theme = models.ManyToManyField(Middle, related_name='stock', blank=True)
    hot = models.BooleanField(default=False)
    memory = models.BooleanField(default=False)

class BigComments(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    located_at = models.ForeignKey(Big, related_name='comments', on_delete=models.CASCADE)

class MiddleComments(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    located_at = models.ForeignKey(Middle, related_name='comments', on_delete=models.CASCADE)

class StockComments(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    located_at = models.ForeignKey(Stock, related_name='comments', on_delete=models.CASCADE)



