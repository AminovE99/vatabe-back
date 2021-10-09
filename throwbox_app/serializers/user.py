from rest_framework import serializers
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer

from throwbox_app.models.users import User


class CreateUserSerializer(serializers.ModelSerializer):
    """Сериализатор для базовой модели пользователя"""

    class Meta:
        model = User
        fields = ('role', 'username')


class CreateResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'role', 'inflation_koeff', 'days_before_payday')

class RetrieveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'money_qty', 'days_before_payday', 'questions', 'events')


class LoginSerializer(RestAuthLoginSerializer):
    username = None
