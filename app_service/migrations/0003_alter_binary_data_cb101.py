# Generated by Django 4.2.4 on 2023-08-31 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_service', '0002_binary_data_remove_kepcoside_cb281_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binary_data',
            name='cb101',
            field=models.BooleanField(null=True),
        ),
    ]
