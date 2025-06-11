from rest_framework import serializers
from planetarium.models import PlanetariumDome, AstronomyShow, ShowSession, ShowTheme


class PlanetariumDomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlanetariumDome
        fields = ("id", "name", "rows", "seats_in_row")


class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "description")


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = ("id", "name")


class ShowSessionSerializer(serializers.ModelSerializer):
    astronomy_show = AstronomyShowSerializer(read_only=True)
    planetarium_dome = PlanetariumDomeSerializer(read_only=True)

    astronomy_show_id = serializers.PrimaryKeyRelatedField(
        queryset=AstronomyShow.objects.all(), write_only=True, source="astronomy_show"
    )
    planetarium_dome_id = serializers.PrimaryKeyRelatedField(
        queryset=PlanetariumDome.objects.all(), write_only=True, source="planetarium_dome"
    )

    class Meta:
        model = ShowSession
        fields = (
            "id",
            "astronomy_show", "astronomy_show_id",
            "planetarium_dome", "planetarium_dome_id",
            "show_time",
        )
