# Generated by Django 2.2 on 2020-01-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_auto_20200110_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='year',
            field=models.IntegerField(default=2000, null=True),
        ),
    ]