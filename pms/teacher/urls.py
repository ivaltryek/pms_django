from django.conf.urls import url
from .views import superuserpage, AddPlacementCreateView,AddPlacementListView

urlpatterns = [
    url(r'^$', superuserpage, name='superuserpage'),
    url(r'^create/$', AddPlacementCreateView.as_view(), name='addplacement'),
    url(r'^view/$', AddPlacementListView.as_view(), name='list'),
]
