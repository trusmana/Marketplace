# Generated by Django 4.0.2 on 2022-05-04 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Jenis_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('mu', models.DateField(auto_now=True)),
                ('cu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='U_JP', to=settings.AUTH_USER_MODEL)),
                ('kelompok', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.jenis_products')),
            ],
            options={
                'db_table': 'Jenis_Products',
            },
        ),
    ]
