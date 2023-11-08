# Generated by Django 4.2.3 on 2023-08-26 10:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_commentpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postcaption',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='CommentPost',
        ),
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
    ]
