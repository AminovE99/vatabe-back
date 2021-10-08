from django.urls import path
from rest_framework.routers import SimpleRouter

from throwbox_app.views.answer import AnswerViewSet
from throwbox_app.views.question import QuestionViewSet
from throwbox_app.views.user import UserViewSet

router = SimpleRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'answer', AnswerViewSet, basename='answer')
external_urls = [path("get-card/", QuestionViewSet.as_view())]

urlpatterns = router.urls + external_urls
