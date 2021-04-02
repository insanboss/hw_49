from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

# Create your views here.
from tracker_app.forms import IssueForm, SimpleSearchForm
from tracker_app.models import Issue, Project
from django.db.models import Q
from django.utils.http import urlencode


class Index(ListView):
    template_name = 'issues/index.html'
    context_object_name = 'issues'
    model = Issue
    ordering = ['-created_at']

    paginate_by = 3
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        context['search'] = self.search_value
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset


class AddIssue(CreateView):
    model = Issue
    template_name = 'issues/issue_create.html'
    form_class = IssueForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        issue = form.save(commit=False)
        issue.project = project
        issue.save()
        form.save_m2m()
        return redirect('project_View', pk=project.pk)


class IssueView(TemplateView):
    template_name = 'issues/issue_view.html'

    def get_context_data(self, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        context = super().get_context_data()
        context['issue'] = issue
        return context


class IssueUpdate(UpdateView):
    model = Issue
    template_name = 'issues/issue_update.html'
    form_class = IssueForm
    context_object_name = 'issue'

    def get_success_url(self):
        return reverse('issue_view', kwargs={'pk': self.object.pk})


class IssueDelete(DeleteView):
    template_name = 'issues/issue_delete.html'
    model = Issue
    context_object_name = 'issue'
    success_url = reverse_lazy('index')
