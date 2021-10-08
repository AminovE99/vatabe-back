from django.db import models


class Answer(models.Model):
    text = models.CharField("Текст ответа", max_length=1024, blank=True)
    money_qty = models.IntegerField()
    reply = models.CharField('Ответ на вопрос', max_length=1024, blank=True)

    def __str__(self):
        return f"{self.text} + {self.reply}"


class Question(models.Model):
    text = models.CharField("Текст вопроса", max_length=1024, blank=False)
    positive_decision_answer = models.ForeignKey('Answer', related_name='positive_decision_question',
                                                 on_delete=models.CASCADE, default=None, null=True, blank=True)
    negative_decision_answer = models.ForeignKey('Answer', related_name='negative_decision_question',
                                                   on_delete=models.CASCADE, default=None, null=True, blank=True)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.text


class Event(models.Model):
    text = models.CharField("Текст события", max_length=1024, blank=False)
    money_qty = models.IntegerField()

    def __str__(self):
        return f"{self.text}"
