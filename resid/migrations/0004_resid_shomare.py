# Generated by Django 2.2.4 on 2019-08-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resid', '0003_auto_20190724_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='resid',
            name='shomare',
            field=models.CharField(max_length=100, null=True, verbose_name='شماره رسید'),
        ),
    ]
