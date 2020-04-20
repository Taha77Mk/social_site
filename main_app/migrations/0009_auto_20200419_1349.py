# Generated by Django 2.2.12 on 2020-04-19 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20200419_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='guild',
            field=models.CharField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), max_length=100),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='users.Profile'),
        ),
    ]
