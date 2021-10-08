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
        fields = '__all__'


class LoginSerializer(RestAuthLoginSerializer):
    username = None
