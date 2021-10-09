from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404

from throwbox_app.models import User
from throwbox_app.serializers import CreateUserSerializer, CreateResponseSerializer

from rest_framework.response import Response


class UserViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin):
    """
    ViewSet для обновления пациентов
    """

    queryset = User.objects.all()

    def get_serializer_class(self):
        return CreateUserSerializer if self.action == 'create' else CreateResponseSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(User, pk=pk)

    def partial_update(self, request, *args, **kwargs):
        return super(UserViewSet, self).partial_update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        user = User.objects.create(role=request.data.get('role'),
                                   username=request.data.get('first_name') + str(User.objects.count()),
                                   first_name=request.data.get('first_name'))
        return Response(CreateResponseSerializer(user).data)
