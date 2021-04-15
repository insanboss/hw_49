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
    ProjectDelete, AddUserToProject,
)

app_name = 'tracker'

urlpatterns = [
    path('issues', Index.as_view(), name='index'),
    path('issue/<int:pk>', IssueView.as_view(), name='issue_view'),
    path('issue/<int:pk>/update/', IssueUpdate.as_view(), name='issue_update'),
    path('issue/<int:pk>/delete/', IssueDelete.as_view(), name='issue_delete'),
    path('', IndexProjects.as_view(), name='index_projects'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_View'),
    path('project/create/', ProjectCreate.as_view(), name='project_create'),
    path('project/<int:pk>/issue_create', AddIssue.as_view(), name='issue_create'),
    path('project/<int:pk>/update/', ProjectUpdate.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDelete.as_view(), name='project_delete'),
    path('project/<int:pk>/user_add/', AddUserToProject.as_view(), name='user_add'),
]