# Generated by Django 2.2 on 2021-12-20 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bamedcacontent', '0002_auto_20211220_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
                ('name', models.CharField(max_length=50)),
                ('members', models.CharField(max_length=50)),
                ('activeTown', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='branch')),
                ('excoPresi', models.CharField(default='', max_length=50)),
                ('excoVP', models.CharField(default='', max_length=50)),
                ('excoSG', models.CharField(default='', max_length=50)),
                ('introPresi', models.CharField(default='', max_length=200)),
                ('introVP', models.CharField(default='', max_length=200)),
                ('introSG', models.CharField(default='', max_length=200)),
                ('presiImage', models.ImageField(default='', upload_to='branch')),
                ('vpImage', models.ImageField(default='', upload_to='branch')),
                ('sgImage', models.ImageField(default='', upload_to='branch')),
            ],
        ),
    ]
