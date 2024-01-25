# Generated by Django 4.2.4 on 2023-08-31 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_service', '0004_alter_binary_data_cb101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analog_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('p_la', models.FloatField()),
                ('p_lb', models.FloatField()),
                ('p_lc', models.FloatField()),
                ('p_ln', models.FloatField()),
                ('p_va', models.FloatField()),
                ('p_vb', models.FloatField()),
                ('p_vc', models.FloatField()),
                ('p_va_b', models.FloatField()),
                ('p_vb_c', models.FloatField()),
                ('p_vc_a', models.FloatField()),
                ('s_la', models.FloatField()),
                ('s_lb', models.FloatField()),
                ('s_lc', models.FloatField()),
            ],
            options={
                'verbose_name': 'Analog_input',
                'db_table': 'tb_Analog_data',
            },
        ),
        migrations.AlterModelOptions(
            name='binary_data',
            options={'verbose_name': 'binary_input'},
        ),
        migrations.RemoveField(
            model_name='binary_data',
            name='name',
        ),
        migrations.AlterModelTable(
            name='binary_data',
            table='tb_binary_data',
        ),
    ]