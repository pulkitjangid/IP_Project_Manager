# Generated by Django 3.1.7 on 2021-05-24 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20210518_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='muser',
            name='Marks',
            field=models.CharField(default='0', max_length=3),
        ),
    ]
