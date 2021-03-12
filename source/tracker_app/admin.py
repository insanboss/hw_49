from django.contrib import admin
from tracker_app.models import Issue, Status, Type
# Register your models here.
admin.site.register(Issue)
admin.site.register(Status)
admin.site.register(Type)
