# Generated by Django 2.2 on 2021-12-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bamedcacontent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchmodel',
            name='excoSG',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='branchmodel',
            name='introSG',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='branchmodel',
            name='sgImage',
            field=models.ImageField(default='', upload_to='branch'),
        ),
        migrations.AddField(
            model_name='branchmodel',
            name='subDescription',
            field=models.CharField(default='', max_length=100),
        ),
    ]
