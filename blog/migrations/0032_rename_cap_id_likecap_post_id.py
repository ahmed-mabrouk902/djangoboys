# Generated by Django 4.2.3 on 2023-08-26 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_likecap'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likecap',
            old_name='cap_id',
            new_name='post_id',
        ),
    ]
