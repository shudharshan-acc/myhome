# Generated by Django 5.1.2 on 2024-10-29 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='quan',
        ),
    ]
