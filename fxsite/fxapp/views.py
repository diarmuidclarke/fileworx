from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def FileWorx_Submit(request):

    context = {
        'title': 'lets be having those files now',
    }

    return render(request, 'fxapp/fx_submit.html', context)
