# Generated by Django 3.2.2 on 2021-05-07 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='location',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='profile',
            name='countrie',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='sexe',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]