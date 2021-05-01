from django.contrib import admin
from .models import FXApprover, FXSource, FXDestination, FXTaskSpec

admin.site.register(FXApprover)
admin.site.register(FXTaskSpec)
admin.site.register(FXSource)
admin.site.register(FXDestination)