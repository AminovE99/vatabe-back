from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets

from throwbox_app.models import User
from throwbox_app.models.question import Answer
from throwbox_app.serializers.answer import AnswerSerializer
from throwbox_app.views.question import user_id


class AnswerViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Answer.objects.all()

    serializer_class = AnswerSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Answer, pk=pk)

    @swagger_auto_schema(manual_parameters=[user_id])
    def retrieve(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        answer = Answer.objects.get(pk=kwargs.get('pk'))
        user.money_qty += answer.money_qty
        user.save()
        super(AnswerViewSet, self).retrieve(request, *args, **kwargs)
