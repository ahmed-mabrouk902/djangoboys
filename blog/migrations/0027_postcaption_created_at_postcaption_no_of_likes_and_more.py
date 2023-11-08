# Generated by Django 4.2.3 on 2023-08-26 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_rename_text_postcaption_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcaption',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='postcaption',
            name='no_of_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='postcaption',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]