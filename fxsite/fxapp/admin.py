from django.contrib import admin
from .models import FXApprover, FXDestination, FXTaskSpec

admin.site.register(FXApprover)
admin.site.register(FXTaskSpec)
admin.site.register(FXDestination)