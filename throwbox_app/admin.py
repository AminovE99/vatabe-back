from django.contrib import admin

from throwbox_app.models import User
from throwbox_app.models.question import Question, Answer, Event

admin.site.register(User)

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Event)
