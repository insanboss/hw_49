from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tracker_app.forms import ProjectForm
from tracker_app.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexProjects(ListView):
    template_name = 'projects/index_projects.html'
    context_object_name = 'projects'
    model = Project
    ordering = 'start_time'


class ProjectView(DetailView):
    template_name = 'projects/project_view.html'
    model = Project
    context_object_name = 'project'


class ProjectCreate(LoginRequiredMixin, CreateView):
    template_name = 'projects/project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_View', kwargs={'pk': self.object.pk})


class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/project_update.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_View', kwargs={'pk': self.object.pk})


class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('tracker:index_projects')
