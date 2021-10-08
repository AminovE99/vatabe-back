from rest_framework import serializers

from throwbox_app.models import Event


class EventSerializer(serializers.ModelSerializer):
    """Сериализатор для базовой модели событий"""

    class Meta:
        model = Event
        fields = '__all__'
