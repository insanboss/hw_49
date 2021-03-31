from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from tracker_app.forms import ProjectForm
from tracker_app.models import Project


class Index_projects(ListView):
    template_name = 'projects/index_projects.html'
    context_object_name = 'projects'
    model = Project
    ordering = 'start_time'


class Project_view(DetailView):
    template_name = 'projects/project_view.html'
    model = Project
    context_object_name = 'project'


class Project_create(CreateView):
    template_name = 'projects/project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_View', kwargs={'pk': self.object.pk})



