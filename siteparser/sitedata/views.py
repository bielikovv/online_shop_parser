from django.shortcuts import render
from .models import *

def show_main_page(request):
    rozetka = RozetkaSite.objects.all()[:10]
    foxtrot = FoxtrotSite.objects.all()[:10]
    allo = AlloSite.objects.all()[:10]
    return render(request, 'sitedata/main_page.html', {'rozetka':rozetka, 'foxtrot':foxtrot, 'allo':allo})
