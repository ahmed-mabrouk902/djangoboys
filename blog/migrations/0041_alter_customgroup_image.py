# Generated by Django 4.2.3 on 2023-09-08 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_alter_customgroup_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customgroup',
            name='image',
            field=models.ImageField(blank=True, upload_to='group_image'),
        ),
    ]
