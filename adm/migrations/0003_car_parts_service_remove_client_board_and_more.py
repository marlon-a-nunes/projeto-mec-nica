# Generated by Django 4.1.5 on 2023-01-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0002_client_type_of_board_alter_client_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(max_length=50)),
                ('car_year', models.CharField(max_length=4)),
                ('type_of_board', models.CharField(choices=[('mercosur', 'Mercosur'), ('old pattern', 'Old Pattern')], max_length=11, null=True)),
                ('board', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_parts', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
                ('parts_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('doing', 'Doing'), ('done', 'Done')], max_length=5)),
                ('service_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='board',
        ),
        migrations.RemoveField(
            model_name='client',
            name='car',
        ),
        migrations.RemoveField(
            model_name='client',
            name='car_year',
        ),
        migrations.RemoveField(
            model_name='client',
            name='description',
        ),
        migrations.RemoveField(
            model_name='client',
            name='done',
        ),
        migrations.RemoveField(
            model_name='client',
            name='service',
        ),
        migrations.RemoveField(
            model_name='client',
            name='type_of_board',
        ),
    ]