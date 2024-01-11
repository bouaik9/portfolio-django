from ast import List
from django.shortcuts import render
from rest_framework.generics import ListAPIView

from app.serializers import PersonalInfoSerializer, ExperienceSerializer, EducationSerializer, ProjectSrializer, SkillSerializer
# Create your views here.
from .models import PersonalInfo, Project, Experience, Education, Skill


class PersonalInfoView(ListAPIView):
    serializer_class = PersonalInfoSerializer
    queryset = PersonalInfo.objects.all()

class ProjectView(ListAPIView):
    serializer_class = ProjectSrializer
    queryset = Project.objects.all()

class ExperienceView(ListAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()

class EducationView(ListAPIView):
    serializer_class = EducationSerializer
    queryset = Education.objects.all()

class SkillView(ListAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()
