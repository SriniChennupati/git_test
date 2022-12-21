from django.db import models

# Create your models here.
class TestModel(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=30)
    
    