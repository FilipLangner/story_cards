from django import forms
from story_cards.models import Team, Flashcard, Deck

class AddTeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'description', 'students']
        # widgets = {'students': forms.HiddenInput}

class AddDeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['name', 'author', 'team']

class AddFlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        exclude = ['date_created']