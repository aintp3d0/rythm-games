from django.db import models
from django.utils.translation import gettext_lazy as _


class Band(models.Model):
    """ Game Bands
    """
    class Meta:
        db_table = 'bd_band'

    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class SongDifficulty(models.TextChoices):
    """ Song Difficultiees
    """
    EASY = 'EASY', _('Easy')
    NORMAL = 'NORMAL', _('Normal')
    HARD = 'HARD', _('Hard')
    EXPERT = 'EXPERT', _('Expert')
    SPECIAL = 'SPECIAL', _('Special')


class Song(models.Model):
    """ Game Songs
    """
    class Meta:
        db_table = 'bd_song'

    id = models.IntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    max_difficulty = models.CharField(
        max_length=7,
        choices=SongDifficulty.choices,
        default=SongDifficulty.EXPERT,
        null=False, blank=False
    )
    band = models.OneToOneField(Band, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.name} :: {self.band}"
