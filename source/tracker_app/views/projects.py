from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tracker_app.forms import ProjectForm, AddUser
from tracker_app.models import Project
from django.contrib.auth.mixins import PermissionRequiredMixin


class IndexProjects(ListView):
    template_name = 'projects/index_projects.html'
    context_object_name = 'projects'
    model = Project
    ordering = 'start_time'


class ProjectView(DetailView):
    template_name = 'projects/project_view.html'
    model = Project
    context_object_name = 'project'


class ProjectCreate(PermissionRequiredMixin, CreateView):
    template_name = 'projects/project_create.html'
    model = Project
    form_class = ProjectForm
    permission_required = 'tracker_app.add_project'

    def form_valid(self, form):
        project = form.save()
        project.user.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('tracker:project_View', kwargs={'pk': self.object.pk})


class ProjectUpdate(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/project_update.html'
    form_class = ProjectForm
    context_object_name = 'project'
    permission_required = 'tracker_app.change_project'

    def get_success_url(self):
        return reverse('tracker:project_View', kwargs={'pk': self.object.pk})


class ProjectDelete(PermissionRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('tracker:index_projects')
    permission_required = 'tracker_app.delete_project'


class AddUserToProject(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'users/add_user.html'
    form_class = AddUser
    context_object_name = 'project'
    permission_required = 'tracker_app.add_user_to_project'

    def get_success_url(self):
        return reverse('tracker:project_View', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().user.all()
