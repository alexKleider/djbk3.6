from django.shortcuts import render, redirect
from entities.models import Entities

def home_page(request):
    if request.method == "POST":
        Entities.objects.create(text=request.POST['entity_text'])
        return redirect('/')

    return render(request, 'home.html')

