from django.conf.urls import urls
from . import views

urlpatterns = [
    urls('expand/', views.index, name='index'),
]