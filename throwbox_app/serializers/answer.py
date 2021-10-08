from rest_framework import serializers

from throwbox_app.models.question import Answer


class AnswerSerializer(serializers.ModelSerializer):
    """Сериализатор для базовой модели пользователя"""

    class Meta:
        model = Answer
        fields = '__all__'
