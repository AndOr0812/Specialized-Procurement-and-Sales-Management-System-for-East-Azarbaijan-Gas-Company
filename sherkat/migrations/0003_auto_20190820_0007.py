# Generated by Django 2.2.4 on 2019-08-20 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sherkat', '0002_auto_20190818_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sherkat',
            name='mob',
            field=models.IntegerField(blank=True, null=True, verbose_name='شماره موبایل'),
        ),
        migrations.AlterField(
            model_name='sherkat',
            name='tel',
            field=models.IntegerField(blank=True, null=True, verbose_name='شماره تلفن'),
        ),
    ]