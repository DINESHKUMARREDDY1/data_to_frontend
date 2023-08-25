from django.shortcuts import render
from app.models import *
from django.http import HttpResponse


# Create your views here.
def insert_topic(request):
    tn=input('enter topic-name:')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('DATA INSERTED')

def insert_webpage(request):
    tn=input('enter topic-name:')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('enter name : ')
    u=input('enter URL : ')
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    to.save()
    return HttpResponse('DATA INSERTED')


def insert_accessrecords(request):
    n=input('topic-name:')
    to=topic.objects.get_or_create(topic_name=n)[0]
    to.save()
    n=input('enter name : ')
    u=input('enter URL : ')
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    to.save()
    a=input('enter author : ')
    e=input('enter email : ')
    wo=webpage.objects.get_or_create(name=wo,author=a,email=e)[0]
    to.save()
    return HttpResponse('DATA INSERTED')




#display data in web page
def display_topic(request):
    QSTO=topic.objects.all()
    d={'QSTO':QSTO }
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO }
    return render(request,'display_webpage.html',d)
