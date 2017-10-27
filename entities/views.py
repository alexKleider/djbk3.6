from django.shortcuts import render, redirect
from entities.models import Entity

def home_page(request):
    if request.method == "POST":
        Entity.objects.create(text=request.POST['entity_text'])
        return redirect('/')

    return render(request, 'home.html')

