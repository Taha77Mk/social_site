# Generated by Django 2.2.12 on 2020-04-18 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_comments_guild'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
    ]
