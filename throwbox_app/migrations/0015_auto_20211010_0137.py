# Generated by Django 3.2.6 on 2021-10-10 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('throwbox_app', '0014_auto_20211009_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
