from django.db import models

# Create your models here.


class Custumer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=25)
    email = models.CharField(max_length=150)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    current_address_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Address(models.Model):
    custumer_id = models.ForeignKey(Custumer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Order(models.Model):
    custumer_id = models.ForeignKey(Custumer, on_delete=models.CASCADE)
    order_time_stamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    shipping_address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Size(models.Model):
    gender = models.CharField(max_length=25)
    category = models.CharField(max_length=25)
    size = models.FloatField()
    size_us = models.FloatField()
    size_uk = models.FloatField()
    size_eu = models.FloatField()


class Colors(models.Model):
    name = models.CharField(max_length=15)
    rgb = models.CharField(max_length=15)


class Articles(models.Model):
    prpduct_id = models.ForeignKey("Products", on_delete=models.CASCADE)
    ean = models.CharField(max_length=200)
    color_id = models.ForeignKey(Colors, on_delete=models.CASCADE)
    size_id = models.ForeignKey(Size, on_delete=models.CASCADE)
    description = models.TextField()
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    reduce_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.IntegerField()
    dicount_percent = models.IntegerField()
    currently_active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Stock(models.Model):
    article_id = models.ForeignKey(Articles, on_delete=models.CASCADE)
    count = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Orderposition(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Articles, on_delete=models.CASCADE)
    amount = models.SmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Lables(models.Model):
    name = models.CharField(max_length=50)
    slug_name = models.SlugField(max_length=50)
    icon = models.ImageField()


class Products(models.Model):
    name = models.CharField(max_length=100)
    lable_id = models.ForeignKey(Lables, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    gender = models.CharField(max_length=25)
    currently_active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)