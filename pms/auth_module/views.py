from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.messages.api import success
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from django.template import RequestContext

from .forms import LoginForm, UserForm

User = get_user_model()

# from .forms import StudentRegister

# Create your views here.



def register_page(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Registred Successfully')
            return redirect("auth_module:login")
        else:
            messages.error(request, 'Entered data does not matched the requirement')
    else:
        user_form = UserForm()
    return render(request, "auth/register.html", {
        'user_form': user_form,
         })


def login_form(request):
    context_instance=RequestContext(request)
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        print("User Logged In?")
        #print(request.user.is_authenticated())
        user = authenticate(username = username, password = password)
       # print(request.POST.get('username'))
        if user is not None:

            login(request, user)
            #print(request.user.is_authenticated())
            request.session['user'] = username
            profile = User.objects.get(username = username)
            request.session['department'] = profile.department
            request.session['unique_id'] = profile.unique_id
            print('dept:',request.session['department'])
            print('id: ',request.session['unique_id'])
            if request.user.is_superuser:
                return redirect('superuser:superuserpage')
            return redirect('index')
        else:
            messages.error(request, 'Oops,Credentials are wrong try again')
    else:
        print('invalid')
    return render(request,"registration/login.html",{'form':form})
