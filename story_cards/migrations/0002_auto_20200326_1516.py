# Generated by Django 3.0.4 on 2020-03-26 15:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('story_cards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deck',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='flashcard',
            old_name='user',
            new_name='author',
        ),
        migrations.AddField(
            model_name='team',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
