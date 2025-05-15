from django.db import models


class PlanetariumDome(models.Model):
    name = models.CharField(max_length=70)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()


class AstronomyShow(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()


class ShowTheme(models.Model):
    name = models.CharField(max_length=70)


class ShowSession(models.Model):
    astronomy_show = models.ForeignKey(AstronomyShow, on_delete=models.CASCADE)
    planetarium_dome = models.ForeignKey(PlanetariumDome, on_delete=models.CASCADE)
    show_time = models.DateTimeField()
