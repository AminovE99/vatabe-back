from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from throwbox_app.models import User
from throwbox_app.serializers import CustomUserDetailSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    """
    ViewSet для получения и обновления пациентов
    """

    queryset = User.objects.all()
    serializer_class = CustomUserDetailSerializer
    permission_classes = [IsAuthenticated, ]
    parser_classes = (MultiPartParser,)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(User, pk=pk)
    def partial_update(self, request, *args, **kwargs):
        return super(UserViewSet, self).partial_update(request, *args, **kwargs)