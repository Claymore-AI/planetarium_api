from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.constraints import UniqueConstraint
from rest_framework.exceptions import ValidationError

from planetarium.models import ShowSession


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="reservations")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.created_at)

class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    show_session = models.ForeignKey(ShowSession, on_delete=models.CASCADE, related_name="tickets")
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="tickets")

    class Meta:
        constraints = [
            UniqueConstraint(fields=["show_session", "row", "seat"], name="unique_ticket")
        ]

    @staticmethod
    def validate_row(row: int, show_session, error_to_raise=ValidationError):
        max_rows = show_session.planetarium_dome.rows
        if not (1 <= row <= max_rows):
            raise error_to_raise({
                "row": f"Row must be in the range [1, {max_rows}]"
            })

    @staticmethod
    def validate_seat(seat: int, show_session, error_to_raise=ValidationError):
        max_seats = show_session.planetarium_dome.seats_in_row
        if not (1 <= seat <= max_seats):
            raise error_to_raise({
                "seat": f"Seat must be in the range [1, {max_seats}]"
            })

    def clean(self):
        self.validate_row(self.row, self.show_session)
        self.validate_seat(self.seat, self.show_session)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"Show '{self.show_session.astronomy_show.title}' "
            f"at {self.show_session.show_time.strftime('%Y-%m-%d %H:%M')} — "
            f"Row {self.row}, Seat {self.seat}"
        )