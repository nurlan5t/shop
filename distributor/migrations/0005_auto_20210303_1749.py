# Generated by Django 3.1.7 on 2021-03-03 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0004_auto_20210303_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='tag',
            new_name='tags',
        ),
    ]