from rest_framework import serializers

from throwbox_app.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для базовой модели пользователя"""

    class Meta:
        model = Question
        fields = '__all__'
