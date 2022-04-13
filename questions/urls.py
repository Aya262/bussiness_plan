from django.urls import path
from .views import *

urlpatterns = [
    path("register/", Registerapi.as_view()),
    path("ListUpdateSection/<int:sec_num>/", ListUpdateSection.as_view()),
]
