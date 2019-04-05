from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import AddPlacementForm, UpdatePlacementForm
from .models import AddPlacement

# Create your views here.


def superuserpage(request):
    return render(request, "superuserpage.html", {})


class AddPlacementCreateView(LoginRequiredMixin,CreateView):
    login_url = 'auth_module:login'
    model = AddPlacement
    # fields = (
    #     'company',
    #     'department',
    #     'due_date',
    # )
    form_class = AddPlacementForm
    template_name = "superuser/addplacement.html"


class AddPlacementListView(LoginRequiredMixin,ListView):
    login_url = 'auth_module:login'
    context_object_name = "placements"
    model = AddPlacement
    template_name = "superuserpage.html"

    def get_queryset(self):
        queryset = super(AddPlacementListView, self).get_queryset()
        try:
            queryset = queryset.filter(department = self.request.session['department'])
        except KeyError:
            raise Exception("Login Required to access this page.")
        return queryset


class AddPlacementDetailView(DetailView):
    context_object_name = "placementdetail"
    model = AddPlacement
    template_name = "superuser/detailview.html"


class AddPlacementUpdateView(LoginRequiredMixin,UpdateView):
    login_url = 'auth_module:login'
    context_object_name = "updateplacement"
    model = AddPlacement
    template_name = "superuser/updateview.html"
    form_class = UpdatePlacementForm


class AddPlacementDeleteView(LoginRequiredMixin,DeleteView):
    login_url = 'auth_module:login'
    context_object_name = 'delplacement'
    model = AddPlacement
    template_name = "superuser/deleteview.html"
    success_url = reverse_lazy("superuser:list")
