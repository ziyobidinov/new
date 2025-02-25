# Generated by Django 5.1 on 2024-08-20 10:05

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=95, scale=None, size=[466, 360], upload_to='gallery/%Y/%m'),
        ),
    ]
