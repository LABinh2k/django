from django.urls import path

from . import views

app_name = 'GIRng'

urlpatterns = [
    path('', views.index, name='index'),
    path('randomize', views.generate, name='randomize'),
    path('team', views.team, name='team'),
]
