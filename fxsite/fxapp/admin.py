from django.contrib import admin
from .models import *

admin.site.register(FXTaskSpec)
admin.site.register(FXSource)
admin.site.register(FXSourceFilesSpec)
admin.site.register(FXDestination)
admin.site.register(FXApprover)
admin.site.register(FXApproval)
