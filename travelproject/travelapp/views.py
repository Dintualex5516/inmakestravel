from django.http import HttpResponse
from django.shortcuts import render
from .models import place, placex


# Create your views here.

def d2(request):
    obj=place.objects.all()
    ob=placex.objects.all()
    return render(request,"index.html",{'result':obj,'results':ob})


#def demo(request):
    #return HttpResponse("Hello worrld")
