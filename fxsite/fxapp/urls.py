from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'src', views.FXSourceViewSet)
router.register(r'dst', views.FXDestinationViewSet)
router.register(r'appr', views.FXApproverViewSet)
router.register(r'task', views.FXTaskSpecViewSet)
router.register(r'appr_by_dest/<str:lib>', views.FXApproverByDestViewSet, basename='appr_by_dest')
router.register(r'appr_by_dest', views.FXApproverByDestViewSet, basename='appr_by_dest')
router.register(r'src_files', views.FXFilesAtSrcViewSet, basename='src_files')
router.register(r'file_meta', views.FXFilesMetaViewSet, basename='file_meta')



app_name = 'fxapp'


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('fx_q/', views.FileWorx_Queue, name='fx_q'),
    path('fxsubmit4/', views.FileWorx_TaskSpecForm, name='fxsubmit4'),
    path('fxsubmit3/', views.FileWorx_Submit3, name='fxsubmit3'),
    path('fxsubmit2/', views.FileWorx_Submit2, name='fxsubmit2'),
    path('fxsubmit/', views.FileWorx_Submit.as_view(), name='fxsubmit'),
    path('', views.index, name='fxappindex'),
]
