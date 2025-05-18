from rest_framework import viewsets
from reservations.models import Reservation, Ticket
from reservations.serializers import (
    ReservationSerializer,
    ReservationCreateSerializer,
    TicketSerializer
)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return ReservationCreateSerializer
        return ReservationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
