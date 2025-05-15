from django.urls import path, include
from reservations.views import ReservationViewSet, TicketViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register("reservations", ReservationViewSet)
router.register("tickets", TicketViewSet)

app_name = "reservations"

urlpatterns = [path("", include(router.urls))]
