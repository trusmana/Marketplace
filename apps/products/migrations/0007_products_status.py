# Generated by Django 4.0.2 on 2022-05-04 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_products_img1_products_img2_products_img3'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='status',
            field=models.CharField(choices=[('1', 'Aktif'), ('2', 'Non Aktif')], default=1, max_length=20),
        ),
    ]