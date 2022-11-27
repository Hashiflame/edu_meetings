from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from users.models import StudentProfile
from .models import Meeting


class MeetingsListView(ListView):
    model = Meeting
    template_name = 'meetings/meetings_list.html'
    context_object_name = 'meetings'
    paginate_by = 2


class MeetingDetailView(DetailView):
    model = Meeting
    template_name = 'meetings/meeting_detail.html'
    context_object_name = 'meeting'


def book(request, id):
    meeting = Meeting.objects.get(id=id)
    student = StudentProfile.objects.get(user=request.user)
    meeting.listeners.add(student)
    return redirect('main')