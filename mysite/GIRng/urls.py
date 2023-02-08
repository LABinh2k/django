from django.urls import path, include

from . import views

app_name = 'GIRng'

urlpatterns = [
    path('', views.index, name='index'),
    # teams api
    path('teams/random/', views.create_random_team, name='randomize'),
    # team management
    path('teams/add/', views.add_team, name='add-team'),
    path('teams', views.team_list, name='team-list'),
    path('teams/<int:team_id>/', views.team_detail, name='team-detail'),
    # path('teams/update/', TODO)
    # characters management
    path('characters/',
         views.CharacterListView.as_view(),
         name='characters-list'),
    path('characters/<int:pk>/',
         views.CharacterDetailView.as_view(),
         name='character-detail'),
    # path('characters/add/', TODO, TODO),
    # path('characters/update/', TODO)
    # path('characters/delete/', TODO)
    # 
    # auth
    path('accounts/', include('django.contrib.auth.urls')),
]
