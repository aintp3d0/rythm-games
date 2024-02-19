from django.db import models


__all__ = (
    'Band',
)


class Band(models.Model):
    """ Game Bands
    """
    class Meta:
        db_table = 'bd_band'

    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

