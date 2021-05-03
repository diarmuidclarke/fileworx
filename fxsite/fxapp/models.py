from django.db import models
from django.db.models.base import Model
from django.forms.fields import BooleanField
import datetime


class FXSource(models.Model):
    source_path = models.CharField(
        max_length=300,
        verbose_name='Doc Source folder',
        blank = False
    )

    source_path_friendlyname = models.CharField(
        max_length=300,
        verbose_name='Doc Source folder friendly name',
        blank = False
    )


    class Meta:
        verbose_name = 'Source Folder'
        verbose_name_plural = 'Source Folders'
        ordering = ['source_path_friendlyname']


    def __str__(self):
        return self.source_path_friendlyname


class FXDestination(models.Model):

    # TODO - django built in type FileField may be better for this?
    dest_path = models.CharField(
        max_length=300,
        verbose_name='Destination folder'
    )

    dest_path_friendlyname = models.CharField(
        max_length=300,
        verbose_name='Doc Destination folder friendly name',
        blank = False
    )


    class Meta:
        verbose_name = 'File Destination'
        verbose_name_plural = 'File Destinations'
        ordering = ['dest_path_friendlyname']


    def __str__(self):
        return self.dest_path_friendlyname



class FXApprover(models.Model):
    approver_userac = models.CharField(
        max_length=10,
        verbose_name='Approver user account'
    )

    dest = models.ManyToManyField(
        FXDestination, related_name='fxapprover'
    )

    class Meta:
        verbose_name = 'Approver'
        verbose_name_plural = 'Approvers'
        ordering = ['approver_userac']

    def __str__(self):
        return self.approver_userac





class FXTaskSpec(models.Model):
    raised_date  = models.DateField(
        verbose_name='Date raised',
        default = datetime.datetime.now,
        blank=True
    )

    raised_by_userac = models.CharField(
        max_length=10,
        verbose_name='Raised by user',
        help_text='User account of the person raising this request'
    )

    file_source_doc_path = models.ForeignKey(
        FXSource,
        on_delete=models.CASCADE
    )

    # doc_selector = models.FilePathField('File to submit', path = 'E:\\data\\_090_PROJECTS\\_009_CURRENT\\FileWorx\\test_data\\cat1\\', recursive=True)

    dest = models.ForeignKey(
        FXDestination,
        on_delete=models.CASCADE
    )


    
    class Meta:
        verbose_name = 'Task Specification'
        verbose_name_plural = 'Task Specifications'
        ordering = ['raised_date']



    def __str__(self):
        return 'raised by : ' + self.raised_by_userac
