# Generated by Django 5.1 on 2024-08-31 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bamedcacontent', '0020_aboutmodel_paragraph1_aboutmodel_paragraph2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='paragraph1',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='paragraph2',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='paragraph3',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='paragraph1',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='paragraph2',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='eventmodel',
            name='paragraph3',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='paragraph1',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='paragraph2',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='paragraph3',
            field=models.CharField(max_length=1500),
        ),
    ]
