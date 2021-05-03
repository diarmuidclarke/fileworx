from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'src', views.FXSourceViewSet)
router.register(r'dst', views.FXDestinationViewSet)
router.register(r'appr', views.FXApproverViewSet)
router.register(r'task', views.FXTaskSpecViewSet)



app_name = 'fxapp'


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('fxsubmit4/', views.FileWorx_API_Test, name='fxsubmit3'),
    path('fxsubmit3/', views.FileWorx_Submit3, name='fxsubmit3'),
    path('fxsubmit2/', views.FileWorx_Submit2, name='fxsubmit2'),
    path('fxsubmit/', views.FileWorx_Submit.as_view(), name='fxsubmit'),
    path('', views.index, name='fxappindex'),
]
