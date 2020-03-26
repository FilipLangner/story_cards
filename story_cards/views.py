from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from story_cards.forms import AddTeamForm


class AddTeamView(generic.CreateView):
    form_class = AddTeamForm
    template_name = "add_team.html"
    success_url = reverse_lazy('list_teams')
