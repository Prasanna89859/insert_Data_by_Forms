from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def inser_topicname(request):
    ETFO=TopicForms()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForms(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('inser_topicname is done.....')
    return render(request,'inser_topicname.html',d)


def webpages_create(request):
    EWPO=WebpageForms()
    d={'EWPO':EWPO} 
    if request.method =='POST':
        WFDO=WebpageForms(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('webpage is created.....')
    return render(request,'webpages_create.html',d)

def Access_Record(request):
    ARDO=AccessRecordForms()
    d={'ARDO':ARDO}
    if request.method =='POST':
        AFDO=AccessRecordForms(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('AccessRecord is successfully.....')
    return render(request,'Access_Record.html',d)







