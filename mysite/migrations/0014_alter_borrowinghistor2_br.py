# Generated by Django 4.2.6 on 2024-01-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_alter_borrowinghistor2_br'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowinghistor2',
            name='br',
            field=models.CharField(choices=[('B', '借'), ('H', '還')], max_length=1),
        ),
    ]