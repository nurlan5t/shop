# Generated by Django 3.1.7 on 2021-03-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0002_auto_20210303_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='distributor.Tag'),
        ),
    ]
