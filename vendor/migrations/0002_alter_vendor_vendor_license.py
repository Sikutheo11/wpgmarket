# Generated by Django 4.2.4 on 2023-09-07 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_license',
            field=models.FileField(upload_to='media/vendor/license'),
        ),
    ]
