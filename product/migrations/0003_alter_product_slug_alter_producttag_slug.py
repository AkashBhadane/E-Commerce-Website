# Generated by Django 4.2.1 on 2023-06-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_productcategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='producttag',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
