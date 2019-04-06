from builtins import ValueError

from django.apps import apps
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import Http404, HttpResponse, request
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import ApplyPlacement
from .models import RegisterdStudents, StudentDetails

AddPlacementModel = apps.get_model('teacher', 'AddPlacement')
# Create your views here.


class DisplayPlacementListView(LoginRequiredMixin, ListView):
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


class DisplayPlacementDetailView(LoginRequiredMixin, DetailView):
    login_url = 'auth_module:login'
    model = AddPlacementModel
    context_object_name = 'placementdetail'
    template_name = 'student/detailview.html'

    def get_queryset(self):
        queryset = super(DisplayPlacementDetailView, self).get_queryset()
        pk = self.kwargs['pk']
        self.request.session['pkid']=pk
        slugpk = self.kwargs['slug']
        print(pk)
        self.request.session['slugpk'] = slugpk
        print(slugpk)
        print("CompID:",self.request.session['slugpk'])
        return queryset

def ApplyPlacementForm(request):
    student_ids = request.POST.get('registeredstu')
    print("1", student_ids)
    pkid = request.session['pkid']
    comp_id = request.session['slugpk']
    print("CompId In Placeview: ",comp_id)
    try:
        student_details = StudentDetails.objects.get(student_id=student_ids)
        print("2", student_details)
        if request.session["unique_id"] != student_ids:
            raise ValidationError("Given ID didn't match with your current one.!")
        new_registered = RegisterdStudents(registered_student=student_details, slug=comp_id)
        if RegisterdStudents.objects.filter(registered_student=student_details, slug=comp_id):
            raise ValidationError("Already Submitted form, can't do it again")
            exit()
            #messages.error(request, "Already Sent a request, can't do it again.!",extra_tags='error')
            #return redirect('student:listplacement')
        new_registered.save()
        print("SAVED!")
        messages.success(request, "Request sent Successfully")
        return redirect('student:listdetails', pk=pkid, slug=comp_id)
    except StudentDetails.DoesNotExist:
        print("OOPS")
        new_registered = None
    return render(request, "student/applyplacement.html")
