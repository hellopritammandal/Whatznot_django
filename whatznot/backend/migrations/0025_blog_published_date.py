# Generated by Django 4.2.4 on 2023-09-07 22:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0024_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
