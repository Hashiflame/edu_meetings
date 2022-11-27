from django.shortcuts import render, redirect
from django.core.mail import send_mail


def main_view(request):
    return render(request, 'general/index.html')


def contact_view(request):
    if request.POST:
        name = request.POST['name']
        from_email = request.POST['from_email']
        body = request.POST['body']
        subject = request.POST['subject']
        email_message = f'Name: {name}\nFrom email: {from_email}\n{body}'
        send_mail(
            subject,
            email_message,
            'smiron1703@gmail.com',
            ['smiron1703@gmail.com'],
            fail_silently=False,
        )
    return redirect('main')
