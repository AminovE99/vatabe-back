from rest_framework.routers import SimpleRouter

from throwbox_app.views.user import UserViewSet

router = SimpleRouter()
router.register(r'user', UserViewSet, basename='user')


urlpatterns = []
urlpatterns += router.urls
