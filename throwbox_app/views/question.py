from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_INTEGER
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from throwbox_app.models import User
from throwbox_app.serializers import RetrieveUserSerializer
from throwbox_app.serializers.event import EventSerializer
from throwbox_app.serializers.question import QuestionSerializer

user_id = Parameter('user_id', IN_QUERY, 'User id', required=True, type=TYPE_INTEGER)


class QuestionViewSet(APIView):
    """
    ViewSet для обновления пациентов
    """
    serializer_class = QuestionSerializer

    @swagger_auto_schema(
        manual_parameters=[user_id],
    )
    def get(self, request):
        user_id = request.GET.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        user.days_before_payday -= 1
        if user.days_before_payday == 0:
            user.inflation_koeff += 0.1
            user.money_qty += 1000
            user.days_before_payday = 10
        user.save()
        if user.days_before_payday == 5:
            event = user.events.order_by('?').first()
            if not event:
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response({'event': EventSerializer(event).data, 'user': RetrieveUserSerializer(user).data})
        question = user.questions.order_by('?').first()
        if not question:
            return Response(status=status.HTTP_204_NO_CONTENT)
        user.questions.remove(question)
        return Response({'question': QuestionSerializer(question).data, 'user': RetrieveUserSerializer(user).data},
                        status=status.HTTP_200_OK)
