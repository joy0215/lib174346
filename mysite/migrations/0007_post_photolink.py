# Generated by Django 4.2.5 on 2023-11-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_alter_post_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photolink',
            field=models.TextField(blank=True, default=''),
        ),
    ]
