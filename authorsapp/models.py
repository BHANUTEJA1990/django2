from django.db import models
# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=20)
    language=models.CharField(max_length=20,null=True)

    class Meta:
        db_table="book"
class Author(models.Model):
    fn=models.CharField(max_length=20)
    ln=models.CharField(max_length=20,null=True)
    book=models.ManyToManyField(Book,null=True,related_name="authora")
    class Meta:
        db_table="author"
