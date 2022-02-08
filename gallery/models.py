from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null = False, blank = False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null = False, blank = False)
    description = models.TextField()
    # id=models.TextField(max_length=55, primary_key=True)
    
    def __str__(self):
        return self.description