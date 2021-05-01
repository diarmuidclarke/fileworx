# Generated by Django 3.2 on 2021-05-01 18:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FXDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest_path', models.CharField(max_length=300, verbose_name='Destination folder')),
                ('dest_path_friendlyname', models.CharField(max_length=300, verbose_name='Doc Destination folder friendly name')),
            ],
            options={
                'verbose_name': 'File Destination',
                'verbose_name_plural': 'File Destinations',
                'ordering': ['dest_path_friendlyname'],
            },
        ),
        migrations.CreateModel(
            name='FXSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_path', models.CharField(max_length=300, verbose_name='Doc Source folder')),
                ('source_path_friendlyname', models.CharField(max_length=300, verbose_name='Doc Source folder friendly name')),
            ],
            options={
                'verbose_name': 'Source Folder',
                'verbose_name_plural': 'Source Folders',
                'ordering': ['source_path_friendlyname'],
            },
        ),
        migrations.CreateModel(
            name='FXTaskSpec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raised_date', models.DateField(blank=True, default=datetime.datetime.now, verbose_name='Date raised')),
                ('raised_by_userac', models.CharField(help_text='User account of the person raising this request', max_length=10, verbose_name='Raised by user')),
                ('dest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fxapp.fxdestination')),
                ('file_source_doc_path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fxapp.fxsource')),
            ],
            options={
                'verbose_name': 'Task Specification',
                'verbose_name_plural': 'Task Specifications',
                'ordering': ['raised_date'],
            },
        ),
        migrations.CreateModel(
            name='FXApprover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approver_userac', models.CharField(max_length=10, verbose_name='Approver user account')),
                ('dest', models.ManyToManyField(related_name='approver', to='fxapp.FXDestination')),
            ],
            options={
                'verbose_name': 'Approver',
                'verbose_name_plural': 'Approvers',
                'ordering': ['approver_userac'],
            },
        ),
    ]