# Generated by Django 2.2 on 2019-04-03 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='owner',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]