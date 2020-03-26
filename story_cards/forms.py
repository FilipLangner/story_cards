from django import forms
from story_cards.models import Team, Flashcard, Deck

class AddTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'description', 'students']
        # widgets = {'students': forms.HiddenInput}