from django.conf import settings
from django.db import models


# Create your models here.


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=False)
    address = models.CharField(max_length=100, blank=True, null=False)
    phone_number = models.CharField(max_length=10, blank=True, null=False, unique=True)
    opening_time = models.FloatField(blank=True, null=False)
    closing_time = models.FloatField(blank=True, null=False)
    city = models.ForeignKey('City', db_column='city', blank=True, null=False, on_delete=models.DO_NOTHING, db_constraint=False)
    country = models.ForeignKey('Country', db_column='country', blank=True, null=False, on_delete=models.DO_NOTHING, db_constraint=False)
    menu = models.ForeignKey('MenuOfRestaurant', db_column='menu', blank=True, null=False, on_delete=models.DO_NOTHING, db_constraint=False)

    def __str__(self):
        return f'Welcome to the {self.name}'

    class Meta:
        db_table = 'restaurant'
        managed = False


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'country'
        managed = False


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    id_of_country = models.ForeignKey(Country, db_column='id_of_country', blank=True, null=False,
                                      on_delete=models.DO_NOTHING, db_constraint=False)

    class Meta:
        db_table = 'city'
        managed = False


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, blank=True, null=False)
    middle_name = models.CharField(max_length=30, blank=False, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=False)
    phone_number = models.CharField(max_length=10, blank=True, null=False, unique=True)
    email = models.EmailField(max_length=70, blank=True, null=False, unique=True)
    address = models.CharField(max_length=100, blank=True, null=False)
    career = models.CharField(max_length=50, blank=True, null=False)
    salary = models.FloatField(blank=True, null=False)
    restaurant = models.ForeignKey(Restaurant, db_column='restaurant', blank=True, null=False,
                                   on_delete=models.DO_NOTHING, db_constraint=False)

    class Meta:
        db_table = 'employee'
        managed = False


class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, unique=True, null=False)
    components = models.TextField(blank=True, null=False)
    cooking_time = models.FloatField(blank=True, null=False)
    weight = models.IntegerField(blank=True, null=False)
    price = models.FloatField(blank=True, null=False)

    class Meta:
        db_table = 'dish'
        managed = False


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    dish_id = models.ForeignKey(Dish, db_column='dish_id', on_delete=models.DO_NOTHING, db_constraint=False)

    class Meta:
        db_table = 'menu'
        managed = False


class MenuOfRestaurant(models.Model):
    menu_id = models.ForeignKey(Menu, db_column='menu_id', blank=True, null=False, on_delete=models.DO_NOTHING, db_constraint=False)
    dish_id = models.ForeignKey(Dish, db_column='dish_id', blank=True, null=False, on_delete=models.DO_NOTHING, db_constraint=False)

    class Meta:
        db_table = 'menu_of_restaurant'
        managed = False
        verbose_name = "order"
