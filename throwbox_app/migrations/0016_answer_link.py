# Generated by Django 3.2.6 on 2021-10-10 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('throwbox_app', '0015_auto_20211010_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='link',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Ссылка'),
        ),
    ]
