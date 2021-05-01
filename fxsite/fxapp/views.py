# from fxsite.fxapp.models import FXTaskSpecfrom .forms import FXSubmitTaskForm
from .models import FXTaskSpec
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FXSubmitTaskForm


def index(request):
    # return HttpResponse("Hello, world. You're at the FileWorx index.")
    context = {}
    return render(request, 'fxapp/fxapp_index.html',context)




class FileWorx_Submit(LoginRequiredMixin, CreateView):
    login_url = '/fxapp'
    template_name = 'fxapp/fx_submit.html'
    form_class = FXSubmitTaskForm

    # model = FXTaskSpec




    def get_success_url(self):
        return './'


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user']=self.request.user
        return kwargs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'lets be having those files now'
        return context


    # return render(request, 'fxapp/fx_submit.html', context)
    def post(self, request, *args, **kwargs):
        if 'fxsubmit' in request.POST:
            pass
            

        return HttpResponseRedirect(self.get_success_url())



