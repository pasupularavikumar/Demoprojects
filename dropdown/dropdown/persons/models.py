from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class school(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Person,on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=4)
    classroom = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    def __str__(self):
        return self.name




class Demo1(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Demo2(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()

    def __str__(self):
        return self.name
class Info(Demo1):
    class Meta:
        proxy = True
"""
class Place(models.Model):
  class Meta:
    abstract = False
    proxy = False

class Staff(models.Model):
  users = models.ManyToManyField(User)

  class Meta:
    abstract = False
    proxy = False

class Restaurant(Place, Staff):
  class Meta:
    abstract = False
    proxy = False  """