# Generated by Django 4.2.2 on 2023-07-01 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
    ]