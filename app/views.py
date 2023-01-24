from django.shortcuts import render

# Create your views here.
from app.models import *

def display_topics(request):
    QST=Topic.objects.all()
    d={'topics':QST }
    return render(request,'display_topics.html',d)

def dis_webpages(request):
    QSW=Webpage.objects.all()
    d={'web':QSW}
    return render(request,'dis_webpages.html',d)

def dis_access(request):
    QSA=AccessRecords.objects.all()
    d={'venky':QSA}
    return render(request,'dis_access.html',d)
