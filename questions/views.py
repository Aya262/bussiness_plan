from telnetlib import STATUS
from django.shortcuts import render
from rest_framework import generics, status
from .serilaizer import (
    RegisterSerializer,
    SectionQuestionsSerializer,
)
from rest_framework.response import Response
from .models import SectionQuestions
from rest_framework.views import APIView
from django.db.models import Q

# Create your views here.


class Registerapi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


class ListUpdateSection(APIView):
    def get(self, request, sec_num):
        questions = SectionQuestions.objects.filter(section_num=sec_num)
        serializer = SectionQuestionsSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, sec_num):
        instance = SectionQuestions.objects.filter(
            Q(section_num=sec_num) & Q(user=request.user)
        )
        if not instance:
            return Response(
                {"Object does not exists"}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = SectionQuestionsSerializer(
            instance=instance, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
