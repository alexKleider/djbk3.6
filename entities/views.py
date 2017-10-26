from django.shortcuts import render
from entities.models import Entity

def home_page(request):
    entity = Entity()
    entity.text = request.POST.get('entity_text', '')
    entity.save()

    return render(request, 'home.html',
        {'new_entity_text': request.POST.get("entity_text", ''),
        })

