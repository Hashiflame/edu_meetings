from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, reverse

from general.decorators import login_forbidden

from .forms import SignupForm
from .models import *


@login_forbidden
def register(request):
    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
            )
            user.set_password(form.cleaned_data['password1'])
            user.save()
            is_mentor = True if request.POST['is_mentor'] == 'True' else False
            if is_mentor:
                print('mentor')
                MentorProfile.objects.create(user=user)
                my_group = Group.objects.get(name='mentor')
                my_group.user_set.add(user)
                user.is_staff = True
                user.save()
            else:
                student = StudentProfile.objects.create(user=user)
            return redirect(reverse('main'))
        else:
            messages.add_message(request, messages.ERROR, form.errors['__all__'].as_text())
    form = SignupForm()
    context = {
        'form': form,
        'auth': True,
        'is_mentor': request.path.endswith('mentor')
    }
    return render(request, 'users/register.html', context=context)
