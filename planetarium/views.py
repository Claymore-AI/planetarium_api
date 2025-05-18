from rest_framework import viewsets
from planetarium.models import PlanetariumDome, AstronomyShow, ShowSession, ShowTheme
from planetarium.permissions import IsAdminOrIfIsAuthenticatedReadOnly

from planetarium.serializers import (
    PlanetariumDomeSerializer,
    AstronomyShowSerializer,
    ShowThemeSerializer,
    ShowSessionSerializer,
)


class PlanetariumDomeViewSet(viewsets.ModelViewSet):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer
    permission_classes = [IsAdminOrIfIsAuthenticatedReadOnly]


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer
    permission_classes = [IsAdminOrIfIsAuthenticatedReadOnly]


class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer
    permission_classes = [IsAdminOrIfIsAuthenticatedReadOnly]


class ShowSessionViewSet(viewsets.ModelViewSet):
    queryset = ShowSession.objects.all()
    serializer_class = ShowSessionSerializer
    permission_classes = [IsAdminOrIfIsAuthenticatedReadOnly]
