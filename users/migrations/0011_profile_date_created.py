# Generated by Django 2.2.12 on 2020-04-17 15:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_profile_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
