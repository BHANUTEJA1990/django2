from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

from django.core.validators import MaxValueValidator,MinValueValidator
from .validatore import Validate_age

# Create your models here.
class Jobsearch(models.Model):
    name=models.CharField(max_length=20)
    role=models.CharField(max_length=20)
    location =models.CharField(max_length=15,null=True)
    salary=models.IntegerField(5000000)
    notice_period=models.IntegerField(default=0,validators=[MaxValueValidator(30),MinValueValidator(0)])
    age=models.IntegerField(default=2000,validators=[Validate_age])
    #email=models.EmailField(max_length=30)

    objects=models.Manager()


    def __str__(self):
       return self.role
    class Meta:
        db_table="jobsearch"
        ordering=['name','role']




