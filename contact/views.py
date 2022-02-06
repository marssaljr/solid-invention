from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

# Create your views here.
def contactView(request):
    messageSent = False
    name = ''
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            message = cd['name'] + "\n " + cd['email'] + "\n " + cd['message']
            try:
                send_mail('site', message, settings.DEFAULT_FROM_EMAIL, ['marcaljunior8@gmail.com', 'kittymailru@protonmail.ch'])
                messageSent = True
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    return render(request, 'email.html', {
        'form': form,
        'messageSent': messageSent,
        'name': name,
    })

