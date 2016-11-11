from django.shortcuts import render
from .models import Magazine

# Create your views here.
def all_magazines(request):
    magazine = Magazine.objects.all()
    return render(request, "magazines/magazines.html", {"magazines": magazine})
