from django.shortcuts import render, redirect
from entities.models import Entities

def home_page(request):
    if request.method == "POST":
        Entities.objects.create(text=request.POST['entity_text'])
        return redirect('/entities/the_only_list/')

    entities = Entities.objects.all()
    return render(request, 'home.html',
        {'entities': entities,
        })

def list_view(request):
    entities = Entities.objects.all()
    return render(request, 'home.html',
        {'entities': entities,
        })
