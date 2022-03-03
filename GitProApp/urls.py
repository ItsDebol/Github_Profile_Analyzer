from django.urls import path
from . import views

urlpatterns = [
    path('expand/', views.index, name='index'),
]