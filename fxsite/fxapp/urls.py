from django.urls import path
from . import views


app_name = 'fxapp'


urlpatterns = [
    path('fxsubmit/', views.FileWorx_Submit.as_view(), name='fxsubmit'),
    path('', views.index, name='fxappindex'),
]
