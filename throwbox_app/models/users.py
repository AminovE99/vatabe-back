from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver

from throwbox_app.enums import BaseEnum
from throwbox_app.models.question import Question, Event


class RoleChoice(BaseEnum):
    student = "student"
    average = "average"
    old = "old"


class User(AbstractUser):
    """Абстрактный пользователь"""
    role = models.CharField(
        verbose_name="Роль",
        max_length=30,
        choices=RoleChoice.get_choices(),
        blank=True,
        null=True,
        default=None
    )
    questions = models.ManyToManyField('Question', verbose_name="Вопросы", blank=True)
    events = models.ManyToManyField('Event', verbose_name='События', blank=True)
    money_qty = models.IntegerField(default=1000)
    days_before_payday = models.IntegerField(default=10)
    inflation_koeff = models.FloatField(default=1)


@receiver(models.signals.post_save, sender=User)
def execute_after_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.questions.set(Question.objects.all())
        instance.events.set(Event.objects.all())