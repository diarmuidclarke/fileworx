# from fxsite.fxapp.models import FXTaskSpecfrom .forms import FXSubmitTaskForm
from rest_framework import viewsets
from rest_framework import permissions
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from .models import FXApprover, FXDestination, FXSource, FXTaskSpec
from .forms import FXSubmitTaskForm, FXSubmitDocStage1
from .forms import FXSubmitDocStage1, FXSubmitDocStage2
from .serializers import FXApproverSerializer, FXSourceSerializer, FXDestinationSerializer, FXTaskSpecSerializer
from .utils_file import get_files



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



def FileWorx_API_Test(request):
    data = []
    context = { 'data' : data }
    return render(request, 'fxapp/fx_submit4.html',context)




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

