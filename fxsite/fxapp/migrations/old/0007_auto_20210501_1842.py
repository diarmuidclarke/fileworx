# Generated by Django 3.2 on 2021-05-01 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fxapp', '0006_auto_20210501_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fxsource',
            name='source_paths',
        ),
        migrations.AddField(
            model_name='fxsource',
            name='source_path',
            field=models.CharField(default='tbc', max_length=300, verbose_name='Doc Source folder'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fxsource',
            name='source_path_friendlyname',
            field=models.CharField(default='tbc', max_length=300, verbose_name='Doc Source folder'),
            preserve_default=False,
        ),
    ]
