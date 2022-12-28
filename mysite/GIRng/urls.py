from django.urls import path

from . import views

app_name = 'GIRng'

urlpatterns = [
    path('', views.index, name='index'),
    path('team', views.generate, name='team')
]
