from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

# Create your views here.
def contactView(request):
    messageSent = False
    name = ""
    if request.method == "GET":
        form = ContactForm()
        HttpResponse(status=200)
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd["name"]
            message = cd["name"] + "\n " + cd["email"] + "\n " + cd["message"]
            send_mail(
                "site",
                message,
                settings.DEFAULT_FROM_EMAIL,
                ["marcaljunior8@gmail.com", "kittymailru@protonmail.ch"],
                fail_silently=True,
            )
            messageSent = True
            return render(
                request,
                "email.html",
                {
                    "name": name,
                    "form": form,
                    "messageSent": messageSent,
                },
                status=200,
            )
        else:
            messageSent = False
            return render(
                request,
                "email.html",
                {
                    "form": form,
                    "messageSent": messageSent,
                    "error": "You make some mistakes",
                },
                status=400,
            )

    return render(
        request,
        "email.html",
        {
            "form": form,
            "messageSent": messageSent,
            "name": name,
        },
    )
