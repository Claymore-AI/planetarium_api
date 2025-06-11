from django.urls import path, include
from planetarium.views import (
    PlanetariumDomeViewSet,
    AstronomyShowViewSet,
    ShowThemeViewSet,
    ShowSessionViewSet,
)
from rest_framework import routers

router = routers.DefaultRouter()

router.register("planetarium_domes", PlanetariumDomeViewSet)
router.register("astronomy_shows", AstronomyShowViewSet)
router.register("show_themes", ShowThemeViewSet)
router.register("show_sessions", ShowSessionViewSet)

app_name = "planetarium"

urlpatterns = [path("", include(router.urls))]
