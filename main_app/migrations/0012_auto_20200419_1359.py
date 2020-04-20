# Generated by Django 2.2.12 on 2020-04-19 13:59

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20200419_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='guild',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(default=users.models.Profile, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]
