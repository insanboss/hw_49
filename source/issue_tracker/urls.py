"""issue_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tracker_app.views import (
    Index,
    AddIssue,
    IssueView,
    IssueUpdate,
    IssueDelete,
    IndexProjects,
    ProjectView,
    ProjectCreate,
    ProjectUpdate,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('issues', Index.as_view(), name='index'),
    path('issue/<int:pk>', IssueView.as_view(), name='issue_view'),
    path('issue/<int:pk>/update/', IssueUpdate.as_view(), name='issue_update'),
    path('issue/<int:pk>/delete/', IssueDelete.as_view(), name='issue_delete'),
    path('', IndexProjects.as_view(), name='index_projects'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_View'),
    path('project/create/', ProjectCreate.as_view(), name='project_create'),
    path('project/<int:pk>/issue_create', AddIssue.as_view(), name='issue_create'),
    path('project/<int:pk>/update/', ProjectUpdate.as_view(), name='project_update'),
]
