"""Final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include

from story_cards import views

app_name = 'story_cards'
urlpatterns = [
    path('add_team/', views.AddTeamView.as_view(), name='add-team'),
    path('team_detail/<int:team_id>/', views.ShowTeamDetailView.as_view(), name='team-detail'),
    path('deck_detail/<int:deck_id>/', views.ShowDeckDetailView.as_view(), name='deck-detail'),
    path('teams/', views.ListAllTeamsView.as_view(), name='list-teams'),
    path('user_teams/', views.ListLoggedUserTeamsView.as_view(), name='list-user-teams'),
    path('decks/', views.ListAllDecksView.as_view(), name='list-decks'),
    path('edit_team/<int:team_id>/', views.EditTeamView.as_view(), name='edit-team'),
    path('add_deck/<int:team_id>/', views.AddDeckView.as_view(), name='add-deck'),
    path('add_flashcard/<int:team_id>/<int:deck_id>/', views.AddFlashcardView.as_view(), name='add-flashcard'),
    path('edit_flashcard/<int:team_id>/<int:deck_id>/<int:flashcard_id>/', views.EditFlashcardView.as_view(),
         name='edit-flashcard'),
    path('edit_deck/<int:team_id>/<int:deck_id>/', views.EditDeckView.as_view(), name='edit-deck'),
    path('delete_flashcard/<int:team_id>/<int:deck_id>/<int:flashcard_id>/', views.DeleteFlashcardView.as_view(),
         name='delete-flashcard'),
    path('play/<int:deck_id>/', views.PlayStoryCardsView.as_view(), name='play-storycards'),
    path('learn_flashcards/<int:deck_id>/', views.LearnFlashcardsView.as_view(), name='learn-flashcards'),
    path('user_decks/', views.ListLoggedUserDecksView.as_view(), name='list-user-decks'),
    path('search/', views.MySearchView.as_view(), name='search-deck'),
]
