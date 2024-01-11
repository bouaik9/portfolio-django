from django.urls import path

from app.models import Education
from .views import EducationView, ExperienceView, PersonalInfoView, ProjectView, SkillView
urlpatterns = [
    path('personal-info', PersonalInfoView.as_view()),
    path('projects', ProjectView.as_view()),
    path('experience', ExperienceView.as_view()),
    path('education', EducationView.as_view()),
    path('skills', SkillView.as_view())
]