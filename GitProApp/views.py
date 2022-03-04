from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.contrib import sessions
import requests
import json
from multiprocessing.pool import ThreadPool


def index(request):
    response = requests.get('https://api.github.com/users/ItsDebol')  
    content = response.json()
    return JsonResponse(content, safe=False)
   



def rendering(request): 
    if 'data' not in sessions:
        return render("index.html")
    else:
        return render("main.html",data=sessions['data'],graph_y=sessions['graph_y'])
    
    
    
    
def get_user(request) -> json:
    response = requests.get('https://api.github.com/users/ItsDebol')  
    content = response.json()
    userinfo = {"name": content["name"],"email":content["email"], "bio":content["bio"], "followers":content["followers"], "following":content["following"], "Total Number of Public Repos":content["public_repos"]  }
    return JsonResponse(userinfo)
    