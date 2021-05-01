from django.db import models
from django.db.models.base import Model





class FXDestination(models.Model):

    # TODO - django built in type FileField may be better for this?
    file_to_move_path = models.CharField(
        max_length=300,
        verbose_name='Destination folder'
    )


    class Meta:
        verbose_name = 'File Destination'
        verbose_name_plural = 'File Destinations'
    
    def __str__(self):
        return self.file_to_move_path



class FXApprover(models.Model):
    approver_userac = models.CharField(
        max_length=10,
        verbose_name='Approver user account'
    )

    dest = models.ForeignKey(
        FXDestination, related_name='approver',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Approver'
        verbose_name_plural = 'Approvers'
    
    def __str__(self):
        return self.approver_userac



class FXSource(models.Model):
    file_source = models.CharField(
        max_length=300,
        verbose_name='Source Files or Dir',
        help_text=''
    )

    class Meta:
        verbose_name = 'File Source'
        verbose_name_plural = 'File Sources'

    def __str__(self):
        return self.file_source




class FXTaskSpec(models.Model):
    raised_by_userac = models.CharField(
        max_length=10,
        verbose_name='Raised by user',
        help_text='User account of the person raising this request'
    )

    source = models.ForeignKey(
        FXSource,
        on_delete=models.CASCADE
    )

    dest = models.ForeignKey(
        FXDestination,
        on_delete=models.CASCADE
    )
    
    
    class Meta:
        verbose_name = 'Task Specification'
        verbose_name_plural = 'Task Specifications'
    
    def __str__(self):
        return 'raised by : ' + self.raised_by_userac
