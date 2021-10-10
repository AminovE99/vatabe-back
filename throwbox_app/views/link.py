from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from throwbox_app.models import User


class AddLinkView(APIView):
    """
    APIVIew для карточек
    """

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["phone", "first_name", "surname", "patronymic"],
            properties={
                "user_id": openapi.Schema(type=openapi.TYPE_STRING),
                "link": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
    )
    def post(self, request):
        user_id = request.data.get('user_id')
        link = request.data.get('link')
        user = get_object_or_404(User, pk=user_id)
        if not user.links:
            user.links = f"{link},"
        else:
            user.links += f"{link},"
        user.save()