from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    title = models.CharField( max_length=100, verbose_name='titulo')
    description = models.TextField(blank=True, verbose_name='description')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    datecompleted = models.DateTimeField(null=True, verbose_name='fecha completado')
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' by ' + self.user.username

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
