from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from story_cards.forms import AddTeamForm, AddDeckForm, AddFlashcardForm
from story_cards.models import Team, Deck, Flashcard


class AddTeamView(generic.CreateView):
    form_class = AddTeamForm
    template_name = "add_team.html"


class ListAllTeamsView(generic.ListView):
    model = Team
    template_name = "list_all_teams.html"
    context_object_name = "team_list"
    queryset = Team.objects.all().order_by('name')


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
