from builtins import ValueError

from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.http import Http404
from .forms import ApplyPlacement
from .models import RegisterdStudents, StudentDetails

AddPlacementModel = apps.get_model('teacher','AddPlacement')
# Create your views here.


class DisplayPlacementListView(LoginRequiredMixin,ListView):
    login_url = 'auth_module:login'
    model = AddPlacementModel
    context_object_name = 'placelist'
    template_name = 'index.html'

    def get_queryset(self):
        queryset = super(DisplayPlacementListView, self).get_queryset()
        try:
            queryset = queryset.filter(department = self.request.session['department'])
        except KeyError:
            raise Exception("Required Login To Access This Page")
        return queryset

class DisplayPlacementDetailView(LoginRequiredMixin,DetailView):
    login_url = 'auth_module:login'
    model = AddPlacementModel
    context_object_name = 'placementdetail'
    template_name = 'student/detailview.html'

def ApplyPlacementForm(request):
    student_ids = request.POST.get('registeredstu')
    print("1",student_ids)
    try:
        student_details = StudentDetails.objects.get(student_id=student_ids)
        print("2",student_details)
        new_registered = RegisterdStudents(registered_student = student_details)
        if RegisterdStudents.objects.get(registered_student = student_details):
            raise ValueError("Already Submitted form, can't do it again")
        else:
            new_registered.save()
    except StudentDetails.DoesNotExist:
        print("OOPS")
        new_registered = None
    return render(request,"student/applyplacement.html")