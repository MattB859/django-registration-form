from django.core.mail import send_mail
from django.shortcuts import render, redirect



def registration_form(request):
    return render(request, "form/form.html")
