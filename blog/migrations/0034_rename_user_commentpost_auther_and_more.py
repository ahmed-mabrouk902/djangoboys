# Generated by Django 4.2.3 on 2023-08-28 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_commentpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentpost',
            old_name='user',
            new_name='auther',
        ),
        migrations.RenameField(
            model_name='commentpost',
            old_name='caption',
            new_name='com',
        ),
    ]
