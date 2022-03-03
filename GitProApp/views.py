from django.shortcuts import render, HttpResponse
import requests
import json

def index(request):
    yoko = requests.get('https://api.github.com/users/ItsDebol')
    content = yoko.text
    return HttpResponse(content)

def rendering(request):
    return render(request,'index.html')