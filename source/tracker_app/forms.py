from django import forms

from tracker_app.models import Status, Type


class IssueForm(forms.Form):
    summary = forms.CharField(max_length=50, required=True)
    description = forms.CharField(max_length=2000, required=False, widget=forms.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelMultipleChoiceField(required=False, label='Типы', queryset=Type.objects.all())
