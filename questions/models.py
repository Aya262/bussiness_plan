from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    # user = models.ManyToManyField(User)
    # section = models.PositiveIntegerField(default=1, blank=False, null=False)
    title = models.CharField(max_length=150, blank=False, null=False)

    class Meta:
        abstract = True


class Answer(models.Model):
    # user = models.OneToOneField(
    #    User, on_delete=models.DO_NOTHING, blank=True, null=True
    # )
    title = models.CharField(max_length=150, blank=False, null=False)

    class Meta:
        abstract = True


class ChoiceAnswer(Answer):
    choice = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ChoiceQuestion(Question):
    answer = models.ManyToManyField(ChoiceAnswer)

    def __str__(self):
        return self.title


class ValueAnswer(Answer):
    value = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class ValueQuestion(Question):
    answer = models.ForeignKey(ValueAnswer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# main
class SectionQuestions(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    section_num = models.IntegerField(unique=True)
    questions = models.ManyToManyField(ChoiceQuestion)

    def __str__(self):
        return "Section {} ".format(self.section_num)
