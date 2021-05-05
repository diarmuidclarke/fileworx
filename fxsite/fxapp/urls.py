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
router.register(r'new_task', views.FXFilesNewTaskViewSet, basename='new_task')
router.register(r'approve_task', views.FXFilesApproveTaskViewSet, basename='approve_task')
router.register(r'cancel_task', views.FXFilesCancelTaskViewSet, basename='cancel_task')



app_name = 'fxapp'


urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('fx_taskdetail/<pk>/', views.FileWorx_TaskDetail.as_view(), name='fx_taskdetail'),
    path('fx_q/', views.FileWorx_Queue.as_view(), name='fx_q'),
    path('fxsubmit4/', views.FileWorx_TaskSpecForm, name='fxsubmit4'),
    path('fxsubmit3/', views.FileWorx_Submit3, name='fxsubmit3'),
    path('fxsubmit2/', views.FileWorx_Submit2, name='fxsubmit2'),
    path('fxsubmit/', views.FileWorx_Submit.as_view(), name='fxsubmit'),
    path('', views.index, name='fxappindex'),
]
