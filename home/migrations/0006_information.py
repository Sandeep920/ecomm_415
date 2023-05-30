# Generated by Django 4.1.7 on 2023-04-10 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_cart_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=300)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
