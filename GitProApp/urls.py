from django.conf.urls import urls
import views

urlpatterns = [
    urls(r'^$', views.index, name='index'),
]