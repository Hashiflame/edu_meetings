from django.urls import path

from .views import MeetingsListView, MeetingDetailView

app_name = 'meetings'
urlpatterns = [
    path('', MeetingsListView.as_view(), name='meetings-list'),
    path('detail/<slug:slug>', MeetingDetailView.as_view(), name='meeting-detail'),
]

