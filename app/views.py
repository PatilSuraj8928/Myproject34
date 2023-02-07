from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.


def validators(request):
    NFO=NameForm()
    d={'form':NFO}

    if request.method=='POST':
        FD=NameForm(request.POST)
        if FD.is_valid():

            return HttpResponse(str(FD.cleaned_data))
    return render(request, 'validators.html',d)