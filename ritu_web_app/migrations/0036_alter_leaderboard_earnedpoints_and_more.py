# Generated by Django 4.0.5 on 2022-08-30 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ritu_web_app', '0035_alter_leaderboard_earnedpoints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboard',
            name='earnedPoints',
            field=models.FloatField(blank=True, null=True, verbose_name='Points'),
        ),
        migrations.AlterField(
            model_name='task1text',
            name='earnedPoints',
            field=models.FloatField(blank=True, null=True, verbose_name='Points'),
        ),
        migrations.AlterField(
            model_name='task2text',
            name='earnedPoints',
            field=models.FloatField(blank=True, null=True, verbose_name='Points'),
        ),
        migrations.AlterField(
            model_name='task3text',
            name='earnedPoints',
            field=models.FloatField(blank=True, null=True, verbose_name='Points'),
        ),
    ]
