# Generated by Django 3.2.20 on 2023-08-13 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230728_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blankbro.jpg', upload_to='media'),
        ),
    ]