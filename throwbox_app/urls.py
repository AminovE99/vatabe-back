from django.urls import path
from rest_framework.routers import SimpleRouter

from throwbox_app.views.answer import AnswerViewSet
from throwbox_app.views.link import AddLinkView
from throwbox_app.views.question import QuestionViewSet, CardViewSet
from throwbox_app.views.user import UserViewSet

router = SimpleRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'answer', AnswerViewSet, basename='answer')
router.register(r'question', QuestionViewSet, basename='question')
router.register(r'event', QuestionViewSet, basename='event')

external_urls = [path("get-card/", CardViewSet.as_view()),
                 path("add-link/", AddLinkView.as_view())]

urlpatterns = router.urls + external_urls
