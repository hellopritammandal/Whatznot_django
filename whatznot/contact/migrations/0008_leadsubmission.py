# Generated by Django 4.2.4 on 2023-09-09 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_delete_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('budget', models.CharField(choices=[('NoIdea', "I Don't Have Any Idea"), ('3000-10000', '₹ 3000 - ₹ 10000'), ('10000-40000', '₹ 10000 - ₹ 400000'), ('40000-100000', '₹ 40000 - ₹ 100000'), ('100000up', '₹ 100000 And More')], max_length=20, verbose_name='Budget')),
                ('newsletter_subscription', models.BooleanField(default=False, verbose_name='Newsletter Subscription')),
                ('submission_date', models.DateTimeField(auto_now_add=True, verbose_name='Submission Date')),
            ],
            options={
                'verbose_name_plural': 'Lead Form Submissions',
            },
        ),
    ]
