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
        widgets = {
            'author': forms.HiddenInput,
            'team': forms.HiddenInput
        }

class AddFlashcardForm(forms.ModelForm):
    hint = forms.CharField(max_length=256, widget=forms.TextInput(attrs={
        'placeholder': 'Input a synonym or a hint',
    }))
    class Meta:
        model = Flashcard
        exclude = ['date_created']
        widgets = {
            'author': forms.HiddenInput,
            'deck': forms.HiddenInput
        }