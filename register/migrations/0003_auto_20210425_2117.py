# Generated by Django 3.1.7 on 2021-04-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20210425_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Description',
            field=models.TextField(),
        ),
    ]
