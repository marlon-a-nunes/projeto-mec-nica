# Generated by Django 4.1.5 on 2023-01-27 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0004_car_client_service_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='parts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='parts',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
