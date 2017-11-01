from django.shortcuts import render, redirect
from entities.models import Entities

def home_page(request):
    if request.method == "POST":
        Entities.objects.create(text=request.POST['entity_text'])
        return redirect('/entities/the_only_listing/')

    entities = Entities.objects.all()
    return render(request, 'home.html',
        {'entities': entities,
        })

def view_list(request):
    entities = Entities.objects.all()
    return render(request, 'listing.html',
        {'entities': entities,
        })
