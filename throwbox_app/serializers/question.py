from rest_framework import serializers

from throwbox_app.models import Question
from throwbox_app.serializers.answer import AnswerSerializer


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для базовой модели пользователя"""
    positive_decision_answer = AnswerSerializer(read_only=True)
    negative_decision_answer = AnswerSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ('text', 'positive_decision_answer', 'negative_decision_answer', 'warn_about_wrong_decision', 'warning_text', 'order')
