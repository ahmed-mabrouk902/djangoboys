# Generated by Django 3.2.20 on 2023-09-11 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_auto_20230911_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customgroup',
            old_name='id_grp',
            new_name='id',
        ),
    ]
