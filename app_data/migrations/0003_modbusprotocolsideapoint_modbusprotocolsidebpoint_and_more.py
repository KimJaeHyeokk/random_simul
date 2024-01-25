# Generated by Django 4.2.4 on 2023-09-04 10:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_data', '0002_remove_dnp3randombin_datetime_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModbusProtocolSideApoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': '모두버스 프로토컬 사이드 A포인트',
                'db_table': 'tb_modbus_A',
            },
        ),
        migrations.CreateModel(
            name='ModbusProtocolSideBpoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': '모두버스 프로토컬 사이드 B포인트',
                'db_table': 'tb_modbus_B',
            },
        ),
        migrations.CreateModel(
            name='ModbusProtocolSideCpoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': '모두버스 프로토컬 사이드 C포인트',
                'db_table': 'tb_modbus_C',
            },
        ),
    ]
