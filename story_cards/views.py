from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

import random

from story_cards.forms import AddTeamForm, AddDeckForm, AddFlashcardForm, AssignDeckToAnotherTeamForm
from story_cards.models import Team, Deck, Flashcard


class AddTeamView(generic.CreateView):
    form_class = AddTeamForm
    template_name = "add_team.html"
    success_url = reverse_lazy('story-cards:list-teams')


class ListAllTeamsView(generic.ListView):
    model = Team
    template_name = "list_all_teams.html"
    context_object_name = "team_list"
    queryset = Team.objects.all().order_by('name')

class ListLoggedUserTeamsView(generic.ListView):
    model = Team
    template_name = "list_all_teams.html"
    context_object_name = "team_list"

    def get_queryset(self):
        return self.request.user.team_set.order_by('name')


class ListAllDecksView(generic.ListView):
    model = Deck
    template_name = "list_all_decks.html"
    context_object_name = "deck_list"
    queryset = Deck.objects.all().order_by('name')


class ShowTeamDetailView(generic.DetailView):
    template_name = "team_detail.html"
    context_object_name = "team"

    def get_object(self):
        team_id = self.kwargs.get('team_id')
        return get_object_or_404(Team, id=team_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team_id = self.kwargs.get('team_id')
        team = get_object_or_404(Team, id=team_id)
        context['students'] = team.students.all()
        context['decks'] = team.deck_set.all()
        return context

class ShowDeckDetailView(generic.DeleteView):
    template_name = "deck_detail.html"
    context_object_name = "deck"

    def get_object(self, queryset=None):
        deck_id = self.kwargs.get('deck_id')
        return get_object_or_404(Deck, id=deck_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        deck = get_object_or_404(Deck, id=self.kwargs.get('deck_id'))
        context['flashcards'] = deck.flashcard_set.all()
        return context

class EditTeamView(generic.UpdateView):
    form_class = AddTeamForm
    template_name = "add_team.html"
    success_url = reverse_lazy('story-cards:list-teams')

    def get_object(self, queryset=None):
        team_id = self.kwargs.get('team_id')
        return get_object_or_404(Team, id=team_id)


class AddDeckView(generic.CreateView):
    form_class = AddDeckForm
    template_name = 'add_deck.html'

    def get_success_url(self):
        return reverse_lazy('story-cards:add-flashcard', kwargs={
            'team_id': self.kwargs.get('team_id'),
            'deck_id': self.object.id
        })

    def get_initial(self):
        team_from_url = get_object_or_404(Team, id=self.kwargs.get('team_id'))
        logged_in_user = self.request.user
        return {'team': team_from_url, 'author': logged_in_user}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = get_object_or_404(Team, id=self.kwargs.get('team_id'))
        return context


class AddFlashcardView(generic.CreateView):
    form_class = AddFlashcardForm
    template_name = "add_flashcard.html"

    def get_initial(self):
        deck_from_url = get_object_or_404(Deck, id=self.kwargs.get('deck_id'))
        logged_in_user = self.request.user
        return {'deck': deck_from_url, 'author': logged_in_user}

    def get_success_url(self):
        return reverse_lazy('story_cards:edit-deck', kwargs={
            'team_id': self.kwargs.get('team_id'),
            'deck_id': self.kwargs.get('deck_id')
        })

class EditFlashcardView(generic.UpdateView):
    form_class = AddFlashcardForm
    template_name = "add_flashcard.html"
    context_object_name = "flashcard"

    def get_object(self, queryset=None):
        flashcard_id = self.kwargs.get('flashcard_id')
        return get_object_or_404(Flashcard, id=flashcard_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = get_object_or_404(Team, id=self.kwargs.get('team_id'))
        context['deck'] = get_object_or_404(Deck, id=self.kwargs.get('deck_id'))
        return context

    def get_success_url(self):
        return reverse_lazy('story_cards:edit-deck', kwargs={
            'team_id': self.kwargs.get('team_id'),
            'deck_id': self.kwargs.get('deck_id')
        })

class EditDeckView(generic.UpdateView):
    form_class = AddDeckForm
    template_name = "add_deck.html"
    context_object_name = "deck"

    def get_object(self, queryset=None):
        deck_id = self.kwargs.get('deck_id')
        return get_object_or_404(Deck, id=deck_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        deck = get_object_or_404(Deck, id=self.kwargs.get('deck_id'))
        context['flashcards'] = deck.flashcard_set.all()
        context['team'] = get_object_or_404(Team, id=self.kwargs.get('team_id'))
        return context

    def get_success_url(self):
        return reverse_lazy('story-cards:add-flashcard', kwargs={
            'team_id': self.kwargs.get('team_id'),
            'deck_id': self.object.id
        })


class DeleteFlashcardView(generic.DeleteView):
    template_name = "delete_flashcard.html"
    context_object_name = "flashcard"

    def get_object(self, queryset=None):
        flashcard_id = self.kwargs.get('flashcard_id')
        return get_object_or_404(Flashcard, id=flashcard_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = get_object_or_404(Team, id=self.kwargs.get('team_id'))
        context['deck'] = get_object_or_404(Deck, id=self.kwargs.get('deck_id'))
        return context

    def get_success_url(self):
        return reverse_lazy('story-cards:edit-deck', kwargs={
            'team_id': self.kwargs.get('team_id'),
            'deck_id': self.kwargs.get('deck_id')
        })

class PlayStoryCardsView(generic.ListView):
    model = Flashcard
    context_object_name = "flashcard_list"
    template_name = "play_story_cards.html"

    def get_queryset(self):
        current_deck = Deck.objects.get(id=self.kwargs.get('deck_id'))
        flashcard_list = list(Flashcard.objects.filter(deck=current_deck))
        random.shuffle(flashcard_list)
        flashcard_subset = flashcard_list[:3]
        return flashcard_subset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deck'] = Deck.objects.get(id=self.kwargs.get('deck_id'))
        return context

class LearnFlashcardsView(generic.ListView):
    model = Flashcard
    context_object_name = "flashcard_list"
    template_name = "learn_flashcards.html"

    def get_queryset(self):
        current_deck = Deck.objects.get(id=self.kwargs.get('deck_id'))
        flashcards_in_deck = Flashcard.objects.filter(deck=current_deck)
        return flashcards_in_deck

class ListLoggedUserDecksView(generic.ListView):
    model = Deck
    template_name = "list_user_decks.html"
    context_object_name = "deck_list"

    def get_queryset(self):
        return Deck.objects.filter(author=self.request.user).order_by('name')

class MySearchView(generic.ListView):
    model = Deck
    template_name = "list_searched_decks.html"
    context_object_name = "searched_deck_list"

    def get_queryset(self):
        return Deck.objects.filter(name__icontains=self.request.GET.get('deck_phrase'))

class AssignDeckToAnotherTeamView(generic.FormView):
    form_class = AssignDeckToAnotherTeamForm
    template_name = "assign_deck_to_another_team.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def get_initial(self):
        deck_from_url = get_object_or_404(Deck, id=self.kwargs.get('deck_id'))
        logged_in_user = self.request.user
        # user_teams = self.request.user.team_set.order_by('name')
        return {
            'name': deck_from_url.name,
            'author': logged_in_user,
            # 'team': user_teams
        }

    def get_success_url(self):
        pass