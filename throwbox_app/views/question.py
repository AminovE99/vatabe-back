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

from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets

from throwbox_app.models.question import Question, Event


class EventViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Event.objects.all()

    serializer_class = EventSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Event, pk=pk)


class QuestionViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Question.objects.all()

    serializer_class = QuestionSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Question, pk=pk)


class CardViewSet(APIView):
    """
    APIVIew для карточек
    """

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
        question = user.questions.order_by('order').first()
        event = user.events.order_by('order').first()
        if question.order < event.order:
            user.questions.remove(question)
            return Response({'type': 'question', 'object': QuestionSerializer(question).data,
                             'user': RetrieveUserSerializer(user).data},
                            status=status.HTTP_200_OK)
        else:
            user.events.remove(event)
            return Response({'type': 'event', 'object': EventSerializer(event).data,
                             'user': RetrieveUserSerializer(user).data},
                            status=status.HTTP_200_OK)
