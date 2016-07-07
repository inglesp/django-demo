from django.shortcuts import render

from .models import Person


def index_view(request):
    people = Person.objects.all()
    context = {
        'num_people': len(people),
        'people': people,
    }
    return render(request, 'demo/index.html', context)
