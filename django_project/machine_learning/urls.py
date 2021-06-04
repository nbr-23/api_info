
from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('pink_root', views.mavue, name="pink_root"),
    path('api', views.api, name="api")
]