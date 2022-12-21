from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

#custom validator
def name_min_length(value):
    if len(value) < 0:
        raise ValidationError('Name contains only %s but it should contain min 5 chars' %(value))
# Create your models here.

class Test_Model(models.Model):
    name = models.CharField(primary_key=True, 
                            max_length=30, 
                            validators=[name_min_length])
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=30, validators=[MinLengthValidator(5)])
    city = models.CharField(max_length=2, default='CA')