# Generated by Django 5.1.3 on 2025-01-17 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('description', models.TextField()),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.category')),
            ],
            options={
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer', models.CharField(max_length=250)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.product')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('purchase_date', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.customer')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.product')),
                ('total_amount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produits.vente')),
            ],
        ),
    ]
