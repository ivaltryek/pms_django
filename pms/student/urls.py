from django.conf.urls import url
from .views import DisplayPlacementListView, DisplayPlacementDetailView,ApplyPlacementForm
urlpatterns = [
    url(r'^list/$', DisplayPlacementListView.as_view(),name='listplacement'),
    url(r'^list/(?P<pk>\d+)/$', DisplayPlacementDetailView.as_view(), name='listdetails'),
    url(r'^apply/$', ApplyPlacementForm, name='applyform'),

]