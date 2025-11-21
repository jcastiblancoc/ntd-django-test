from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=100, unique=True)
    population = models.CharField(max_length=50, blank=True, null=True)
    terrains = models.JSONField(default=list, blank=True, null=True)
    climates = models.JSONField(default=list, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
