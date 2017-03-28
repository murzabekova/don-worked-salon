from django.shortcuts import render
from models import Slides

# Create your views here.


def index(request):
    slide = Slides.objects.all()
    count = len(Slides.objects.all())
    context = {
        'slides': slide,
        'count': range(count),
        'title': 'Hello',
    }
    return render(request, 'homepage/index.html', context)
