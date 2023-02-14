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
    # path('teams/update/<int:team_id>/', TODO)
    # path('teams/delete/<int:team_id>/, TODO)
    
    # characters management
    path('characters/',
         views.CharacterListView.as_view(),
         name='characters-list'),
    path('characters/<int:pk>/',
         views.CharacterDetailView.as_view(),
         name='character-detail'),
    # path('characters/add/', TODO: add char feature , TODO),
    # path('characters/update/<int:pk>/', TODO: )
    # path('characters/delete/<int:pk>/', TODO)
    
    # artifacts api
    # TODO: artifact management
    
    # weapons api
    # TODO: weapon management
    
    # auth
    path('accounts/', include('django.contrib.auth.urls')),
]
