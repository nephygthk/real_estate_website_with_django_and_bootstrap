# Generated by Django 4.2.2 on 2023-06-28 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ('-created',), 'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterField(
            model_name='media',
            name='property_image',
            field=models.FileField(upload_to='property_images'),
        ),
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='top_image',
            field=models.FileField(blank=True, null=True, upload_to='top_images'),
        ),
    ]
