# Generated by Django 2.2.12 on 2020-04-18 18:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200418_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='replay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guild', models.CharField(blank=True, max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replay', to='main_app.comments')),
            ],
        ),
    ]
