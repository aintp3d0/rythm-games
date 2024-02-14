from django.contrib import admin

from .models import Band, Song


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    """ Admin Band
    """


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    """ Admin Song
    """
