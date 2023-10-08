from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('about-us', views.about, name='opodder'),
    path('create', views.create, name='create'),
    path('registr', views.registr, name='registr')
]