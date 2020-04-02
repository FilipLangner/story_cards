from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone


class User(AbstractUser):

    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    students = models.ManyToManyField(User)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('story-cards:team-detail', kwargs={"team_id": self.id})

class Deck(models.Model):
    name = models.CharField(max_length=128)
    # flashcards = models.ManyToManyField(Flashcard)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('story-cards:deck-detail', kwargs={"deck_id": self.id})

class Flashcard(models.Model):
    source_word = models.CharField(max_length=256)
    target_word = models.CharField(max_length=256)
    example_usage = models.TextField()
    synonym = models.CharField(max_length=256)
    antonym = models.CharField(max_length=256)
    # picture = models.ImageField() TODO adding image as 'should have'
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.source_word} ({self.target_word})'