from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    url(r'^register/',views.register_page,name='register'),
    url(r'^login/',views.login_form,name='login'),
    url(r'^logout/',auth_views.LogoutView.as_view(),{'next_page':'index'},name='logout'),
]
