from django.db import models

# Create your models here.
# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.
class Media(models.Model):
    name=models.CharField(max_length=20)
    type=models.CharField(max_length=20)
    format=models.CharField(max_length=15,null=True)
    size=models.IntegerField(default=0)
    duration_secs=models.IntegerField(default=0)

    image=models.Manager()
    objects=models.Manager()
    songs=models.Manager()

    def __str__(self):
        return self.name
    class Meta:
        db_table="media"
        ordering=['name','type']
