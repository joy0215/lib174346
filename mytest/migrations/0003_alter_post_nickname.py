# Generated by Django 4.2.4 on 2024-01-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytest', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='nickname',
            field=models.CharField(default='匿名', max_length=10),
        ),
    ]
