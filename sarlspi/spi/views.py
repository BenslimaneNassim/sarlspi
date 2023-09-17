from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    context = {}
    # if request.method == "POST":
    #     prenom = request.POST.get('firstname')
    #     nom = request.POST.get('lastname')
    #     nom = prenom + " " + nom
    #     num = request.POST.get('phone')
    #     note = request.POST.get('message')
    #     Devi.objects.create(nom = nom, telephone = num, note = note).save()
    return render(request, "index.html", context)

def project(request):
    context = {}
    if request.method == "POST":
        prenom = request.POST.get('firstname')
        nom = request.POST.get('lastname')
        nom = prenom + " " + nom
        num = request.POST.get('phone')
        note = request.POST.get('message')
        Devi.objects.create(nom = nom, telephone = num, note = note).save()
    images = Image.objects.all()
    blocs = Bloc.objects.all()
    context = {'images':images, 'blocs':blocs}
    return render (request, "about-us.html", context)

def contact(request):
    context = {}
    if request.method == "POST":
        prenom = request.POST.get('firstname')
        nom = request.POST.get('lastname')
        nom = prenom + " " + nom
        num = request.POST.get('phone')
        email = request.POST.get('email')
        note = request.POST.get('message')
        Contact.objects.create(nom = nom, telephone = num, note = note, email = email).save()
    return render (request, "contacts.html", context)
