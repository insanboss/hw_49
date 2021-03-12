from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView

# Create your views here.
from tracker_app.forms import IssueForm
from tracker_app.models import Issue


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        issues = Issue.objects.all()
        context = super().get_context_data()
        context['issues'] = issues
        return context


class AddIssue(View):

    def get(self, request, **kwargs):
        issue = IssueForm()
        return render(request, 'issue_create.html', context={'form': issue})

    def post(self, request, **kwargs):
        issue = IssueForm(data=request.POST)
        if issue.is_valid():
            issue = Issue.objects.create(
                summary=issue.cleaned_data.get('summary'),
                description=issue.cleaned_data.get('description'),
                status=issue.cleaned_data.get('status'),
                type=issue.cleaned_data.get('type'),
            )
        else:
            return render(request, 'issue_create.html', context={'form': issue})
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
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(initial={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status,
            'type': issue.type
        })
        return render(request, 'issue_update.html', context={'form': form, "id": issue.id})

    def post(self, request, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue.summary = form.cleaned_data.get('summary'),
            issue.description = form.cleaned_data.get('description'),
            issue.status = form.cleaned_data.get('status'),
            issue.type = form.cleaned_data.get('type'),

            issue.save()
        else:
            return render(request, 'issue_update.html', context={'form': form, "id": issue.id})
        return redirect('product_view', pk=issue.id)


class IssueDelete(TemplateView):
    template_name = 'issue_delete.html'

    def get(self, request, **kwargs):
        issue = get_object_or_404(Issue, pk=pk)
        return render(request, 'issue_delete.html', context={'issue': issue})

    def post(self, request, **kwargs):
        issue = get_object_or_404(Issue, pk=pk)
        issue.delete()
        return redirect('index')