from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView, ListView

# Create your views here.
from tracker_app.forms import IssueForm, SimpleSearchForm
from tracker_app.models import Issue
from django.db.models import Q
from django.utils.http import urlencode


class Index(ListView):
    template_name = 'index.html'
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


class AddIssue(View):

    def get(self, request, **kwargs):
        print(self.kwargs, request, kwargs)
        form = IssueForm()
        return render(request, 'issue_create.html', context={'form': form})

    def post(self, request, **kwargs):
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue = Issue.objects.create(
                summary=form.cleaned_data.get('summary'),
                description=form.cleaned_data.get('description'),
                status=form.cleaned_data.get('status'),
            )
            issue.type.set(form.cleaned_data.get('type'))
        else:
            return render(request, 'issue_create.html', context={'form': form})
        return redirect('issue_view', pk=issue.id)


class IssueView(TemplateView):
    template_name = 'issue_view.html'

    def get_context_data(self, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        context = super().get_context_data()
        context['issue'] = issue
        return context


class IssueUpdate(TemplateView):
    template_name = 'issue_update.html'

    def get(self, request, **kwargs):
        print(self.kwargs, request, kwargs)
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(initial={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status,
            'type': issue.type.all()
        })
        return render(request, 'issue_update.html', context={'form': form, "id": issue.id})

    def post(self, request, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue.summary = form.cleaned_data.get('summary')
            issue.description = form.cleaned_data.get('description')
            issue.status = form.cleaned_data.get('status')
            issue.type.set(form.cleaned_data.get('type'))

            issue.save()
        else:
            return render(request, 'issue_update.html', context={'form': form, "id": issue.id})
        return redirect('issue_view', pk=issue.id)


class IssueDelete(TemplateView):
    template_name = 'issue_delete.html'

    def get(self, request, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get("pk"))
        return render(request, 'issue_delete.html', context={'issue': issue})

    def post(self, request, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get("pk"))
        issue.delete()
        return redirect('index')
