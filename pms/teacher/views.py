from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .forms import AddPlacementForm
from .models import AddPlacement

# Create your views here.


def superuserpage(request):
    return render(request, "superuserpage.html", {})


class AddPlacementCreateView(CreateView):
    model = AddPlacement
    # fields = (
    #     'company',
    #     'department',
    #     'due_date',
    # )
    form_class = AddPlacementForm
    template_name = "superuser/addplacement.html"


class AddPlacementListView(ListView):
    context_object_name = "placements"
    model = AddPlacement
    template_name = "superuserpage.html"
