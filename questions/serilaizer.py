from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerialier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password"]

    def create(request, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        return user


class ChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceAnswer
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    answer = ChoiceAnswerSerializer(many=True)

    class Meta:
        model = ChoiceQuestion
        fields = "__all__"


class SectionQuestionsSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = SectionQuestions
        fields = "__all__"
