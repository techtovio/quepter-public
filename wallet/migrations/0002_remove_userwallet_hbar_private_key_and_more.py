# Generated by Django 5.1.7 on 2025-03-26 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userwallet',
            name='hbar_private_key',
        ),
        migrations.RemoveField(
            model_name='userwallet',
            name='hbar_public_key',
        ),
    ]
