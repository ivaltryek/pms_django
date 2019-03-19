from django import forms
from .models import AddPlacement

class DateInput(forms.DateInput):
    format_key = 'DATE_INPUT_FORMATS'
    input_type = 'date'


class AddPlacementForm(forms.ModelForm):
    due_date = forms.DateField(label="Due Date",widget = DateInput(attrs={"class":"form-control"}))
    class Meta:
        model = AddPlacement
        fields = (
            'company',
            'department',
            'due_date',
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

        }