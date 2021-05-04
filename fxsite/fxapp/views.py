from rest_framework import viewsets, permissions, request
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework import mixins
from rest_framework import generics
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from .file_meta import get_file_meta
import os
import datetime
from .models import FXApprover, FXDestination, FXSource, FXSourceFilesSpec, FXTaskSpec
from .forms import FXSubmitTaskForm, FXSubmitDocStage1
from .forms import FXSubmitDocStage1, FXSubmitDocStage2
from .serializers import FXApproverSerializer, FXSourceSerializer, FXDestinationSerializer, FXTaskSpecSerializer, fx_files_at_src_Serializer
from .serializers import fx_approverlist_Serializer, fx_files_at_src_Serializer, fx_filemeta_Serializer
from .utils_file import get_files




FX_SUPPORTED_FILES =  ['.docx', '.doc']




class FXSourceViewSet(viewsets.ModelViewSet):
    queryset = FXSource.objects.all().order_by('source_path_friendlyname')
    serializer_class = FXSourceSerializer
    permission_classes = [permissions.IsAuthenticated]

class FXDestinationViewSet(viewsets.ModelViewSet):
    queryset = FXDestination.objects.all().order_by('dest_path_friendlyname')
    serializer_class = FXDestinationSerializer
    permission_classes = [permissions.IsAuthenticated]

class FXApproverViewSet(viewsets.ModelViewSet):
    queryset = FXApprover.objects.all().order_by('approver_userac')
    serializer_class = FXApproverSerializer
    permission_classes = [permissions.IsAuthenticated]

class FXTaskSpecViewSet(viewsets.ModelViewSet):
    queryset = FXTaskSpec.objects.all().order_by('-raised_date')
    serializer_class = FXTaskSpecSerializer
    permission_classes = [permissions.IsAuthenticated]

def index(request):
    context = {}
    return render(request, 'fxapp/fxapp_index.html',context)



def FileWorx_TaskSpecForm(request):

    
    if request.method=='POST':
        
        return HttpResponseRedirect(reverse('fxapp:fx_q'))

    data = []
    context = { 'data' : data }
    return render(request, 'fxapp/fx_submit4.html',context)



# show status of FX Task Queue
def FileWorx_Queue(request):
    data = []
    context = { 'data' : data }
    return render(request, 'fxapp/fx_q.html',context)


# object needed by serialiser fx_approverlist_Serializer
#    can't just give it a raw list
class SerializerInput_ApproverList(object):    
    def __init__(self, apprlist):
        self.apprlist = apprlist

# REST endpoint - list of approvers for a given destination
class FXApproverByDestViewSet(viewsets.ViewSet):

    def list(self, request):
        list_approvers = []

        params = request.query_params
        if len(params) == 0:
            pass
        elif len(params) == 1:
            lib = next(iter(params))
            qs_dest_f = FXDestination.objects.filter(dest_path_friendlyname__icontains = lib)
            for dest_f in qs_dest_f:
                qs_appr = FXApprover.objects.filter(dest = dest_f)
                for appr in qs_appr:
                    list_approvers.append(appr.approver_userac)

        obj = SerializerInput_ApproverList(list_approvers)
        serializer = fx_approverlist_Serializer(instance=obj)
        return Response(serializer.data)


# object needed by serialiser fx_approverlist_Serializer
#    can't just give it a raw list
class SerializerInput_FilesAtSource(object):    
    def __init__(self, filelist):
        self.filelist = filelist


# REST endpoint - list of files at a given source
# https://medium.com/django-rest-framework/django-rest-framework-viewset-when-you-don-t-have-a-model-335a0490ba6f
class FXFilesAtSrcViewSet(viewsets.ViewSet):

    def list(self, request):
        list_files = []
        params = request.query_params
        if len(params) == 1:
            src = next(iter(params))
            qs_src_f = FXSource.objects.filter(source_path_friendlyname__icontains = src)
            if len(qs_src_f) == 1:
                srcmodel = qs_src_f[0]
                list_files = get_files(srcmodel.source_path, FX_SUPPORTED_FILES)

        obj = SerializerInput_FilesAtSource(list_files)
        serializer = fx_files_at_src_Serializer(instance=obj)
        return Response(serializer.data)


# object needed by serialiser fx_filemeta_Serializer
class SerializerInput_FileMeta(object):    
    def __init__(self, dictmeta):
        self.dictmeta = dictmeta


# REST endpoint - doc metadata including analysis
class FXFilesMetaViewSet(viewsets.ViewSet):

    def list(self, request):
        dictmeta = {}
        params = request.query_params
        if len(params) == 2:
            # get the full path
            filename = params['file']
            src = params['src_f']
            qs_src_f = FXSource.objects.filter(source_path_friendlyname__icontains = src)
            if len(qs_src_f) == 1:
                srcmodel = qs_src_f[0]
            path = os.path.join(srcmodel.source_path, filename)
            dictmeta = get_file_meta(path)

        obj = SerializerInput_FileMeta(dictmeta)
        serializer = fx_filemeta_Serializer(instance=obj)
        return Response(serializer.data)



# REST endpoint - create new Task, using info from form
# api_view(['POST'])
class FXFilesNewTaskViewSet(viewsets.ViewSet):

    def list(self, request):
        dictmeta = {}
        params = request.query_params
        if len(params) == 6:
            fxtask = FXTaskSpec()
            fxtask.raised_by_userac = params['raised_by']
            dateobj = datetime.datetime.strptime(params['raised'], "%Y-%m-%d")
            fxtask.raised_date = dateobj
            
            srcobj = FXSource.objects.get(source_path_friendlyname = params['src_f'])
            fxtask.file_source_doc_path = srcobj

            fxss = FXSourceFilesSpec()
            fxss.file_source = srcobj
            fxss.file_spec_kind = 'ONE'
            filter_str = ''
            for fil in FX_SUPPORTED_FILES:
                filter_str += fil + ','
            fxss.file_spec_filter = filter_str
            fxss.file_name = params['file']
            fxss.save()

            fxtask.file_source_spec = fxss
            
            dstobj = FXDestination.objects.get(
                dest_path_friendlyname = params['dest_f'])
            fxtask.dest = dstobj
            
            fxtask.task_stage = 'QUEUED'
            fxtask.task_status_ok = True # so far!
            fxtask.save()
            
        content = {'please move along': 'nothing to see here'}
        return Response(content, status=status.HTTP_200_OK)
        

    # def get_extra_actions():
    #     pass


def FileWorx_Submit3(request):
    form = FXSubmitDocStage2()



    if request.method=='POST':
        form = FXSubmitDocStage2(request.POST)

    context = { 'form' : form }

    return render(request, 'fxapp/fx_submit3.html',context)



def FileWorx_Submit2(request):
    form = FXSubmitDocStage1()
    
    if request.method=='POST':
        form = FXSubmitDocStage1(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            date = cd.get('raised_date')
            cache.set('dit:stage1:date', date)

            user = cd.get('raised_by')
            cache.set('dit:stage1:user', user)

            src = cd.get('choice_source')
            cache.set('dit:stage1:src', src)
            
            ## success
            context = {}
            # return render(request, 'fxapp/fx_submit3.html',context)
            return HttpResponseRedirect(reverse('fxapp:fxsubmit3'))


    context = { 'form' : form }

    return render(request, 'fxapp/fx_submit2.html',context)


class FileWorx_Submit(LoginRequiredMixin, CreateView):
    login_url = '/fxapp'
    template_name = 'fxapp/fx_submit.html'
    form_class = FXSubmitDocStage1

    # model = FXTaskSpec




    def get_success_url(self):
        return './'


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'lets be having those files now'
    #     return context


    # # return render(request, 'fxapp/fx_submit.html', context)
    # def post(self, request, *args, **kwargs):
    #     if 'fxsubmit' in request.POST:
    #         pass
    #     return HttpResponseRedirect(self.get_success_url())


    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def form_valid(self, form):
        # set up the cache of files

        # create the task spec
        return HttpResponseRedirect(self.get_success_url())

