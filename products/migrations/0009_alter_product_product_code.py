# Generated by Django 3.2.9 on 2021-12-07 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(blank=True, default=0, max_length=10),
        ),
    ]
