# Generated by Django 4.2.3 on 2023-09-08 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_alter_customgroup_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customgroup',
            name='Games',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='customgroup',
            name='location',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
