from django.shortcuts import render

# Create your views here.
def animals(request):
    return render(request,'animals.html')

def birds(request):
    return render(request,'birds.html')
