
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('fxapp/', include('fxapp.urls')),
    path('admin/', admin.site.urls),
    # path('select2/', include('django_select2.urls')),
]
