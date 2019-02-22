from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'cwApp/index.html')


def details(request):
    return render(request, 'cwApp/base.html')



def about(request):
    return render(request, 'cwApp/about.html')