# Generated by Django 3.2.9 on 2021-12-05 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20211204_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Required and unique', max_length=255, unique=True, verbose_name='Category Name'),
        ),
    ]
