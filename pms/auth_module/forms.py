from django import forms
from .models import Teacher
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()


# class StudentRegister(UserCreationForm):
#     email = forms.EmailField(required=True)
#     department = forms.CharField(max_length=2)
#     contact = forms.IntegerField()
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'password1',
#             'password2',
#             )
#     def save(self, commit=True):
#         user = super(StudentRegister,self).save(commit=False)
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']
#         user.password1 = self.cleaned_data['password1']
#         user.password2 = self.cleaned_data['password2']
#         user.department = self.cleaned_data['department']
#         user.contact = self.cleaned_data['contact']

#         if commit:
#             user.save()
#         return user

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget = forms.EmailInput(
        attrs={
            "class":"form-control",
            "id":"email",
        }
    ))

    department = forms.CharField(required = True,widget = forms.TextInput(
        attrs={
            "class":"form-control",
            "id":"department",
        }
    ))
    contact = forms.IntegerField(required=True, widget = forms.NumberInput(
        attrs={
            "class":"form-control",
            "id":"contact",
        }
    ))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'department',
            'contact',
        )

        widgets = {
            'username': forms.TextInput(attrs = {
                "class":"form-control",
                "id":"username",
            }
            ),
            'first_name':forms.TextInput(attrs={
                "class":"form-control",
                "id":"first_name",
            }
            ),
            'last_name':forms.TextInput(attrs={
                "class":"form-control",
                "id":"last_name",
            }
            ),
            'password1': forms.PasswordInput(attrs={
                "class":"form-control",
                "id":"password1",

            }),
            'password2': forms.PasswordInput(attrs={
                "class":"form-control",
                "id":"password2",
            })
        }

class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(
        attrs={
            "class":"form-control",
            "id":"form_full_name",
            "placeholder":"Enter Your Name"

        }
    )
    )
    password = forms.CharField(label="Password",widget = forms.PasswordInput(attrs={
            "class":"form-control",
            "id":"form_full_name",
            "placeholder":"Enter Your Password"
        }
    ))
