from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ChoiceQuestion)
admin.site.register(ValueQuestion)
admin.site.register(ChoiceAnswer)
admin.site.register(ValueAnswer)
admin.site.register(SectionQuestions)
