# Generated by Django 4.1.7 on 2023-04-01 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_productreview_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productreview',
            name='checkout',
        ),
    ]
