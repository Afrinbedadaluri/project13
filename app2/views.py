from django.shortcuts import render

# Create your views here.
def reptils(request):
    return render(request,'reptils.html')

def fishes(request):
    return render(request,'fishes.html')

