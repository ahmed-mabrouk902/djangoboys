# Generated by Django 4.2.3 on 2023-08-22 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_alter_form_request_disponibilité_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='BGimg',
            field=models.ImageField(default='timeline-1.jpg', upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='form_request',
            name='Email',
            field=models.EmailField(default='@gmail.com', max_length=254),
        ),
    ]
