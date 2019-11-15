from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Philosophy, Mission, Vision, Virtues, Prayer, PhysicalAddress, MailingAddress, ContactPerson, ExtraContact, DrivingDirection


# Create your views here.
def home(request):

    return render(request, 'pages/home.html')

def about(request):

    p = Philosophy.objects.all()
    m = Mission.objects.all()
    vis = Vision.objects.all()
    vir = Virtues.objects.all()
    pray = Prayer.objects.all()
    context = {
      'phil': p,
      'mis' : m,
      'vis' : vis,
      'vir' : vir,
      'pray' : pray
     }


    return render(request, 'pages/about.html', context) #{'title':'About'},

def contactus(request):

    p = PhysicalAddress.objects.all()
    m = MailingAddress.objects.all()
    c = ContactPerson.objects.all()
    e = ExtraContact.objects.all()
    d = DrivingDirection.objects.all()
    context = {
      'p': p,
      'm' : m,
      'c' : c,
      'e' : e,
      'd': d,
     }


    return render(request, 'pages/contactus.html', context) #{'title':'About'},


#class AboutListView(ListView):
#    model =
