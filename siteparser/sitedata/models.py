from django.db import models


class RozetkaSite(models.Model):
    title = models.CharField(max_length=500, verbose_name='Title')
    price = models.CharField(max_length=100, verbose_name='Price')
    link = models.CharField(max_length=555, verbose_name='Link')
    reviews = models.CharField(max_length=30, verbose_name='Reviews', null=True)
    image_link = models.CharField(max_length=555, verbose_name='Image link', null=True)



class FoxtrotSite(models.Model):
    title = models.CharField(max_length=500, verbose_name='Title')
    price = models.CharField(max_length=100, verbose_name='Price')
    link = models.CharField(max_length=555, verbose_name='Link')
    reviews = models.CharField(max_length=30, verbose_name='Reviews', null=True)
    image_link = models.CharField(max_length=555, verbose_name='Image link', null=True)



class AlloSite(models.Model):
    title = models.CharField(max_length=500, verbose_name='Title')
    price = models.CharField(max_length=100, verbose_name='Price')
    link = models.CharField(max_length=555, verbose_name='Link')
    reviews = models.CharField(max_length=30, verbose_name='Reviews', null=True)
    image_link = models.CharField(max_length=555, verbose_name='Image link', null=True)



