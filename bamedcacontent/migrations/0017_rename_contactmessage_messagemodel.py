# Generated by Django 5.1 on 2024-08-30 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bamedcacontent', '0016_contactmessage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactMessage',
            new_name='MessageModel',
        ),
    ]
