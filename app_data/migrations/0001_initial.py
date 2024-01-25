# Generated by Django 4.2.4 on 2023-08-31 16:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalogDefinition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': '아날로그 데이터 정의',
                'db_table': 'tb_analog_def',
            },
        ),
        migrations.CreateModel(
            name='BinaryDefinition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': '바이너리 데이터 정의',
                'db_table': 'tb_bin_def',
            },
        ),
        migrations.CreateModel(
            name='Dnp3RandomBin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.BooleanField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('datetime_id', models.IntegerField()),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_data.binarydefinition')),
            ],
            options={
                'verbose_name_plural': 'DNP3 수집 데이터 바이너리',
                'db_table': 'tb_dnp3_random_bin',
            },
        ),
        migrations.CreateModel(
            name='Dnp3RandomAnalog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.FloatField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_data.analogdefinition')),
            ],
            options={
                'verbose_name_plural': 'DNP3 수집 데이터 아날로그',
                'db_table': 'tb_dnp3_random_analog',
            },
        ),
    ]
