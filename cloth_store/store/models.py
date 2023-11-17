from django.db import models


# Create your models here.

class Products(models.Model):
    id = models.OneToOneField('Images', primary_key=True)
    gender = models.CharField(max_length=25)
    master_category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    article_type = models.CharField(max_length=50)
    base_color = models.CharField(max_length=40)
    season = models.CharField(max_length=10)
    year = models.DateField()
    usage = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    is_available = models.BooleanField()


class ProductImages(models.Model):
    id = models.IntegerField(primary_key=True, blank=False)
    product_image = models.ImageField(upload_to="product_image/")


class Users(models.Model):
    user_name = models.CharField(max_length=60)
    user_password = models.CharField(max_length=60)
    user_email = models.EmailField(max_length=100)
    user_phone = models.CharField(max_length=25)
    address = models.CharField(max_length=150)
    admin = models.BooleanField(default=False)
