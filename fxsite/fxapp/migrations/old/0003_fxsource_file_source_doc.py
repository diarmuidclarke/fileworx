# Generated by Django 3.2 on 2021-05-01 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fxapp', '0002_auto_20210501_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='fxsource',
            name='file_source_doc',
            field=models.FileField(default='tbc', help_text='Source document for filing', upload_to='source_docs', verbose_name='Source Doc'),
            preserve_default=False,
        ),
    ]
