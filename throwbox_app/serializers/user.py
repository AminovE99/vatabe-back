from rest_framework import serializers
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer

from throwbox_app.models.users import User


class CreateUserSerializer(serializers.ModelSerializer):
    """Сериализатор для базовой модели пользователя"""

    class Meta:
        model = User
        fields = ('role', 'first_name')


class CreateResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'first_name', 'role', 'inflation_koeff', 'days_before_payday')


class RetrieveUserSerializer(serializers.ModelSerializer):
    questions_qty = serializers.SerializerMethodField()
    events_qty = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('pk', 'money_qty', 'days_before_payday', 'questions_qty', 'events_qty')

    def get_questions_qty(self, obj):
        return obj.questions.count()

    def get_events_qty(self, obj):
        return obj.events.count()


class LoginSerializer(RestAuthLoginSerializer):
    username = None
