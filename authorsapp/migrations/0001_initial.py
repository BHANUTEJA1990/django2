# Generated by Django 4.1.7 on 2023-04-03 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fn', models.CharField(max_length=20)),
                ('ln', models.CharField(max_length=20, null=True)),
                ('book', models.ManyToManyField(null=True, related_name='authora', to='authorsapp.book')),
            ],
            options={
                'db_table': 'author',
            },
        ),
    ]
