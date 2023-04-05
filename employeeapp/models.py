from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator,MinValueValidator
from django.core.exceptions import ValidationError

def gmail_validator(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError('This field only accepts Gmail addresses.')
class Employee(models.Model):
    name=models.CharField(max_length=20)
    salary=models.IntegerField(default=0)
    email =models.EmailField(validators=[gmail_validator])

    objects=models.Manager()
    def __str__(self):
        return self.name

    class Meta:
        db_table="employee"
        ordering=['name','salary']
