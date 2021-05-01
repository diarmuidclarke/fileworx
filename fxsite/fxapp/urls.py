from django.urls import path

from . import views
app_name = 'fxapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('fxsubmit/', views.FileWorx_Submit, name='fxsubmit'),
]
