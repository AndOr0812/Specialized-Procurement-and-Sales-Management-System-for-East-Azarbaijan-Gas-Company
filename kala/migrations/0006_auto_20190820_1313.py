# Generated by Django 2.2.4 on 2019-08-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kala', '0005_auto_20190820_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kala',
            name='estefade',
        ),
        migrations.AlterField(
            model_name='kala',
            name='sharh',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='شرح(مورداستفاده)'),
        ),
    ]
