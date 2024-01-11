from rest_framework.serializers import ModelSerializer

from app.models import Education, Experience, PersonalInfo, Project, Skill

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

class PersonalInfoSerializer(ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = "__all__"


class ProjectSrializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields  = "__all__"

class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"