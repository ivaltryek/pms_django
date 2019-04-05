from django import forms

from .models import RegisterdStudents


class ApplyPlacement(forms.ModelForm):
    registered_student = forms.CharField(required=True, widget = forms.TextInput(
        attrs={
            "class":"form-control",
            "id":"unique_id",
            "placeholder":"Department In Capitals and it follows as issued.!",
        }
    ))


    class Meta:
        model = RegisterdStudents
        fields = (
            'registered_student',
        )
