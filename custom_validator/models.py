# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
def even_validator(value):
    if value % 2 != 0:
        raise ValidationError('This field only accepts even integers.')

def gmail_validator(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError('This field only accepts Gmail addresses.')
class Int_Char(models.Model):
    even=models.IntegerField(validators=[even_validator])
    email = models.EmailField(validators=[gmail_validator])

    objects=models.Manager()
    def __str__(self):
       return self.email
    class Meta:
        db_table="int_char"
        ordering=['even','email']




