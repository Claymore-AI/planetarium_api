from django.db import models


class PlanetariumDome(models.Model):
    name = models.CharField(max_length=70)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return f"{self.name} — {self.rows} rows × {self.seats_in_row} seats"

class AstronomyShow(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()

    def __str__(self):
        return self.title

class ShowTheme(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class ShowSession(models.Model):
    astronomy_show = models.ForeignKey(AstronomyShow, on_delete=models.CASCADE, related_name="show_sessions")
    planetarium_dome = models.ForeignKey(PlanetariumDome, on_delete=models.CASCADE, related_name="show_sessions")
    show_time = models.DateTimeField()

    def __str__(self):
        return (
            f"{self.astronomy_show.title} in {self.planetarium_dome.name} "
            f"at {self.show_time.strftime('%Y-%m-%d %H:%M')}"
        )