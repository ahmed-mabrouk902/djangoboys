# Generated by Django 4.2.3 on 2023-08-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_alter_commentpost_auther_alter_commentpost_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentpost',
            name='auther',
            field=models.CharField(max_length=50),
        ),
    ]