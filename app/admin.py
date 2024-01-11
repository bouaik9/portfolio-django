from django.contrib import admin

from app.models import Education, Experience, PersonalInfo, Project, Skill

# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(Skill)

admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Project)