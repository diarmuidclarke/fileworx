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



class FXSourceFilesSpec(models.Model):
    
    file_source = models.ForeignKey(
        FXSource,
        on_delete=models.CASCADE,
        related_name='src_file_spec'
    )

    FSK_CHOICES = (
        ('ONE', '*ONE* File Specified'),
        ('ALL', '*ALL* Files from the related Source path (top level only)'),
        ('REC', 'All Files from the related Source path (all top level and all found by *REC*ursing into sub dirs)'),
    )
    file_spec_kind = models.CharField(
        max_length=3,
        verbose_name='File Spec Kind',
        choices=FSK_CHOICES,
        blank = False
    )

    # filter in certain files by extension, does not get usedc if file_spec_kind is ONE    
    file_spec_filter= models.CharField(
        max_length=300,
        verbose_name='File Spec Filter', # 
        blank = True, # default to no filter, *.*
        default='*.*' # set to comma or semicolon separated list of filters, e.g. '*.doc;*.docx';*.pdf'
    )

    # if 'ONE' given as file_spec_kind, use this field to store the filename
    file_name = models.CharField(
        max_length=300,
        verbose_name='File name',
        blank = True
    )


    class Meta:
        verbose_name = 'File Source Spec'
        verbose_name_plural = 'File Source Specs'


    def __str__(self):
        if self.file_spec_kind == 'ONE':
            return 'FileSpecKind: ' + str(self.file_spec_kind) + ' from ' + str(self.file_source) + ' --> ' + str(self.file_name)
        else:
            return 'FileSpecKind: ' + str(self.file_spec_kind) + ' from ' + str(self.file_source)




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

    file_source_spec = models.ForeignKey(
        FXSourceFilesSpec,
        on_delete=models.CASCADE,
        null=True
    )

    dest = models.ForeignKey(
        FXDestination,
        on_delete=models.CASCADE
    )

    approved_by = models.ForeignKey(
        FXApprover,
        on_delete=models.CASCADE,
        null= True,
    )
    approved = models.DateField(
        verbose_name='Date approved',
        default = None,
        blank=True,
        null=True
    )


    STAGE_CHOICES = (
        # 12345678901234
        ('DRAFTING',    'Drafting'),
        ('QUEUED',      'Queued up'),
        ('APPROVED',    'Approved'),
        ('COPY.2.LIB',  'Copying to Library'),
        ('GEN.IDX.LIB', 'Updating Index'),
        ('MOVE.2.ARCH', 'Moving previous issue to Library'),
        ('COMPLETE',    'Completed'),
    )
    task_stage = models.CharField(
        max_length=12,
        verbose_name='Task Stage',
        choices=STAGE_CHOICES,
        blank=False,
        default='DRAFTING'
    )

    # error information or just OK
    task_status_ok = models.BooleanField(
        verbose_name='Task Status OK',
        default=True
    )

    task_status_detail = models.CharField(
        max_length=5000,
        verbose_name='Task Status Detail Information',
        blank=True,
        default=''
    )

    class Meta:
        verbose_name = 'Task Specification'
        verbose_name_plural = 'Task Specifications'
        ordering = ['raised_date']

    def __str__(self):
        return 'Task spec raised by : ' + self.raised_by_userac + ' on ' + str(self.raised_date)



class FXApproval(models.Model):

    approver_userac = models.CharField(
        max_length=10,
        verbose_name='Approved by (user account)'
    )
    
    approval_date  = models.DateField(
        verbose_name='Date approved',
        default = datetime.datetime.now,
        blank=True
    )

    task_spec_ref = models.ForeignKey(
        FXTaskSpec,
        on_delete=models.CASCADE,
        related_name='approval'
    )

