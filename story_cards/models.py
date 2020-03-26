from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    students = models.ManyToManyField(User)

class Flashcard(models.Model):
    source_word = models.CharField(max_length=256)
    target_word = models.CharField(max_length=256)
    example_usage = models.TextField()
    synonym = models.CharField(max_length=256)
    antonym = models.CharField(max_length=256)
    # picture = models.ImageField() TODO adding image as 'should have'
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Deck(models.Model):
    name = models.CharField(max_length=128)
    flashcards = models.ManyToManyField(Flashcard)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ManyToManyField(Team)
