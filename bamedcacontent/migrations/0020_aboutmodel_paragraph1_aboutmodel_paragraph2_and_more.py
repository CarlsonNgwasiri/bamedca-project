# Generated by Django 5.1 on 2024-08-31 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bamedcacontent', '0019_quatermodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='paragraph1',
            field=models.CharField(default='sgagdhd bkadubefcu jdfbefbe', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutmodel',
            name='paragraph2',
            field=models.CharField(default='thhedygd shdvdhvud kabdufu', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutmodel',
            name='paragraph3',
            field=models.CharField(default='hdfyrvdvd sbdhvsidb shbdbdu', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='paragraph1',
            field=models.CharField(default='hhdsdu bdhbbdub skbwryubd', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='paragraph2',
            field=models.CharField(default='dvcydfdyey asbcwif ;jnadvd', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventmodel',
            name='paragraph3',
            field=models.CharField(default='sdvfkhd ahbhdehwi shbfbwdu', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='paragraph1',
            field=models.CharField(default='dbwodguf sjbdbuwfu sjbudcbuwd', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='paragraph2',
            field=models.CharField(default='sbdcbubf shdfvhwvd shdhbiw', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='paragraph3',
            field=models.CharField(default='sbchdufr shhidvcywd skbdbu', max_length=100),
            preserve_default=False,
        ),
    ]
