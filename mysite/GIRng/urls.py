from django.urls import path, include

from . import views

app_name = 'GIRng'

urlpatterns = [
    path('', views.index, name='index'),
    path('randomize', views.generate, name='randomize'),
    path('team', views.team, name='team'),
    path('teamlist', views.teamlist, name='team-list'),
    path('<int:team_id>/',views.team_detail, name='team-detail'),
    path('characters/', views.CharacterListView.as_view(), name='characters-list'),
    path('characters/<int:pk>/', views.CharacterDetailView.as_view(), name='character-detail'),
    # auth
    path('accounts/', include('django.contrib.auth.urls')),
    
]
