# Generated by Django 5.0.7 on 2024-10-19 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0011_alter_dress_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.dress')),
            ],
        ),
    ]
