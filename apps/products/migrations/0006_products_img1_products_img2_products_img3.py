# Generated by Django 4.0.2 on 2022-05-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_products_size_products_warna_brand_products_merk'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='products',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
        migrations.AddField(
            model_name='products',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
