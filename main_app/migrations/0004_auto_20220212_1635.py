# Generated by Django 2.2 on 2022-02-12 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20220206_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='rsvp',
            field=models.ManyToManyField(null=True, related_name='user_rsvps', to='main_app.User'),
        ),
    ]
