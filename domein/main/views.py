from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data =  {
        'title': "Главная страница",
        'value':['help', 'setting', 'inform']
    }
    return render(request, 'main/index.html',data)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')
