from django.contrib import admin

from projects.models import Project, Skill, Request, ProjectSkill

admin.site.register(Project)
admin.site.register(ProjectSkill)
admin.site.register(Skill)
admin.site.register(Request)


