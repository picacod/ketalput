# Generated by Django 5.0.7 on 2024-10-04 06:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecommerceapp', '0002_delete_dress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Mens', 'Mens'), ('Womens', 'Womens'), ('Kids', 'Kids')], max_length=20)),
                ('category', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('occasion', models.CharField(choices=[('CASUAL', 'Casual'), ('FORMAL', 'Formal'), ('PARTY', 'Party'), ('WEDDING', 'Wedding'), ('OTHER', 'Other')], max_length=200)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('color', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='dresses/')),
                ('additional_images', models.JSONField(blank=True, null=True)),
                ('stock_quantity', models.PositiveIntegerField(default=0)),
                ('reviews_count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
