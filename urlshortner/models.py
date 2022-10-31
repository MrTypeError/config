from .utils import createShortUrl
from django.db import models


class Shortner(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=20, unique=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} Converted to {self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = createShortUrl(self)
        super().save(*args, **kwargs)
