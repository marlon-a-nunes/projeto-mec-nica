# Generated by Django 4.1.5 on 2023-01-27 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0005_car_created_at_car_update_at_parts_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parts',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adm.car'),
        ),
    ]
