# Generated by Django 3.1 on 2020-08-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0005_productlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]
