from django import forms

from tracker_app.models import Issue


class IssueForm(forms.ModelForm):
    
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'type']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")