from django.shortcuts import render
from entities.models import Entity

def home_page(request):
    if request.method == "POST":
        new_entity_text = request.POST['entity_text']
        Entity.objects.create(text= new_entity_text)
    else:
        new_entity_text = ''

    return render(request, 'home.html',
        {'new_entity_text': new_entity_text,
        })

