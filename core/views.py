from django.shortcuts import render

from .models import Outlet

# Create your views here.

def outlets(request):

    outlets = Outlet.objects.all()

    return render(
        request,
        'outlets.html',
        context={
            'outlets': outlets
        }
    )
