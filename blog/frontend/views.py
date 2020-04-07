from django.shortcuts import render

def index(request):
    """ rendering the page """
    return render(request, 'frontend/index.html')
