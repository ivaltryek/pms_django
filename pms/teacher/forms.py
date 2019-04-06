from django import forms
from django.forms.widgets import URLInput

from .models import AddPlacement


class DateInput(forms.DateInput):
    format_key = 'DATE_INPUT_FORMATS'
    input_type = 'date'


class AddPlacementForm(forms.ModelForm):
    due_date = forms.DateField(label="Due Date",widget = DateInput(attrs={"class":"form-control"}))
    criteria = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    class Meta:
        model = AddPlacement
        fields = (
            'company',
            'department',
            'due_date',
            'company_url',
            'criteria',
        )
        widgets = {
            'company':forms.TextInput(attrs={
                "class":"form-control",
                "id":"company"
            }),

            'department':forms.TextInput(attrs={
                "class":"form-control",
                "id":"department"
            }),

            'due_date':forms.DateInput(attrs={
                "class":"form-control",
                "id":"due_date"
            }),
            'Company URL':forms.URLInput(attrs={
                "class":"form-control",
                "id":"company_url"
            }),
            'Criteria':forms.TextInput(attrs={
                "class":"form-control",
                "id":"criteria"
            }),

        }

class UpdatePlacementForm(forms.ModelForm):
    due_date = forms.DateField(label="Due Date",widget = DateInput(attrs={"class":"form-control"}))
    criteria = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
    company_url = forms.URLField(label="Company URL",widget=URLInput(attrs={"class":"form-control"}))
    class Meta:
        model = AddPlacement
        fields = (
            'company',
            'department',
            'due_date',
            'company_url',
            'criteria',
        )

        widgets = {
            'company':forms.TextInput(attrs={
                "class":"form-control",
                "id":"company"
            }),
            'department':forms.TextInput(attrs={
                "class":"form-control",
                "id":"department"
            }),

            'due_date':forms.DateInput(attrs={
                "class":"form-control",
                "id":"due_date"
            }),
            'Company URL':forms.URLInput(attrs={
                "class":"form-control",
                "id":"company_url"
            }),
            'Criteria':forms.TextInput(attrs={
                "class":"form-control",
                "id":"criteria"
            }),

        }