from django.urls import path
from . import views

urlpatterns = [
    path('expand/', views.index, name='index'),
    path('intro/', views.rendering, name='rendering'),
    path('profile/', views.get_user, name='get_user')
    
]