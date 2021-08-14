from rest_framework import serializers
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer

from throwbox_app.models.users import User


class CustomUserDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для базовой модели пользователя"""

    class Meta:
        model = User
        fields = ('nickname', 'avatar')
        read_only_fields = ('email',)


class LoginSerializer(RestAuthLoginSerializer):
    username = None
