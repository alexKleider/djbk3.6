from django.shortcuts import render, redirect
from entities.models import Entities, List

def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    entities = Entities.objects.filter(list=list_)
    return render(request, 'listing.html',
        {'entities': entities,
        })

def new_list(request):
    list_ = List.objects.create()
    Entities.objects.create(text=request.POST['entity_text'],
        list=list_)
    return redirect(f'/entities/{list_.id}/')

