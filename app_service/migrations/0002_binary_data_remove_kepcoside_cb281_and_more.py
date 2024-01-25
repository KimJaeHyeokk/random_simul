# Generated by Django 4.2.4 on 2023-08-31 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Binary_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('cb101', models.BooleanField()),
                ('es101', models.BooleanField()),
                ('cb102', models.BooleanField()),
                ('es102', models.BooleanField()),
                ('ds111', models.BooleanField()),
                ('es111', models.BooleanField()),
                ('es112', models.BooleanField()),
                ('ds121', models.BooleanField()),
                ('es121', models.BooleanField()),
                ('es122', models.BooleanField()),
                ('cb181', models.BooleanField()),
                ('cb191', models.BooleanField()),
                ('cb281', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='kepcoside',
            name='cb281',
        ),
        migrations.RemoveField(
            model_name='station',
            name='dc_dn_link_ds121',
        ),
        migrations.RemoveField(
            model_name='station',
            name='dc_dn_link_es121',
        ),
        migrations.RemoveField(
            model_name='station',
            name='dc_dn_link_es122',
        ),
        migrations.RemoveField(
            model_name='station',
            name='dc_up_link_ds111',
        ),
        migrations.RemoveField(
            model_name='station',
            name='dc_up_link_es111',
        ),
        migrations.RemoveField(
            model_name='station',
            name='dc_up_link_es112',
        ),
        migrations.RemoveField(
            model_name='station',
            name='transformer_cb101',
        ),
        migrations.RemoveField(
            model_name='station',
            name='transformer_cb102',
        ),
        migrations.RemoveField(
            model_name='station',
            name='transformer_es101',
        ),
        migrations.RemoveField(
            model_name='station',
            name='transformer_es102',
        ),
        migrations.RemoveField(
            model_name='system',
            name='dg_grid',
        ),
        migrations.RemoveField(
            model_name='system',
            name='kepco_side',
        ),
        migrations.RemoveField(
            model_name='system',
            name='station',
        ),
        migrations.DeleteModel(
            name='DGGrid',
        ),
        migrations.DeleteModel(
            name='Equipment',
        ),
        migrations.DeleteModel(
            name='KepcoSide',
        ),
        migrations.DeleteModel(
            name='Station',
        ),
        migrations.DeleteModel(
            name='System',
        ),
    ]