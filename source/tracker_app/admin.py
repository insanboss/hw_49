from django.contrib import admin
from tracker_app.models import Issue, Status, Type, Project
# Register your models here.
admin.site.register(Issue)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)


