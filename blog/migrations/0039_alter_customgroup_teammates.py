# Generated by Django 4.2.3 on 2023-09-08 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_customgroup_joingroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customgroup',
            name='teammates',
            field=models.IntegerField(default=0),
        ),
    ]
