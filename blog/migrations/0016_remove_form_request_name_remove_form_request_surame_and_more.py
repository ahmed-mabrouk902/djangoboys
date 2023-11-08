# Generated by Django 4.2.3 on 2023-08-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_form_request_age_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form_request',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='form_request',
            name='Surame',
        ),
        migrations.AddField(
            model_name='form_request',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='male', max_length=6),
        ),
    ]
