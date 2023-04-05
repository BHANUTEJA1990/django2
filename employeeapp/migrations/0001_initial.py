# Generated by Django 4.1.7 on 2023-04-03 03:07

from django.db import migrations, models
import employeeapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('salary', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254, validators=[employeeapp.models.gmail_validator])),
            ],
            options={
                'db_table': 'employee',
                'ordering': ['name', 'salary'],
            },
        ),
    ]
