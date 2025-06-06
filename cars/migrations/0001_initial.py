# Generated by Django 5.2.1 on 2025-05-31 20:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cars/')),
                ('model', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('new', 'Brand New'), ('used', 'Pre-Owned')], max_length=10)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.brand')),
            ],
        ),
    ]
