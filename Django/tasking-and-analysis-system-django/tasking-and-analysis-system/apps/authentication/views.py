from django.contrib.auth import login, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.auth.models import Permission
from .forms import *
from .helper import encrypt_id, send_invitation, decrypt_id
from .models import User, Role
from ..constants import Fields, AuthenticationFields, General
from apps.audit_trail.models import AuditTrail


def test(request):
    roles = User.objects.last()._meta.fields

    # print(inspect.getmembers(admin.ModelAdmin, predicate=inspect.ismethod))
    print(roles)
    return HttpResponse(roles)


def login_view(request):
    ''' Displays the login form and handles the login action '''
    if request.user.is_authenticated:
        return redirect(General.HOME)

    form = LoginForm(request.POST or None)
    message = None
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get(AuthenticationFields.EMAIL)
            password = form.cleaned_data.get(AuthenticationFields.PASSWORD)
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)

                return redirect(General.HOME)
            else:
                message = 'Invalid credentials'
        else:
            message = 'Error validating the form'

    return render(request,
                  "accounts/login.html",
                  {General.FORM: form, General.MESSAGE: message})


def reset_password(request, hash):
    if request.user.is_authenticated:
        return redirect(General.HOME)
    user_id = decrypt_id(hash)
    try:
        user = User.objects.get(id=user_id)
    except ObjectDoesNotExist:
        return redirect(General.HOME)

    form = PasswordConfirmForm()
    if request.method == "POST":
        form = PasswordConfirmForm(request.POST)

        if form.is_valid():
            password1 = form.cleaned_data.get(AuthenticationFields.PASSWORD1)
            user.set_password(password1)
            user.is_active = True
            user.save()
            return redirect(AuthenticationFields.LOGIN)

    return render(request, "accounts/confirm_password.html", {General.FORM: form})


def forgot_password(request):
    if request.user.is_authenticated:
        return redirect(General.HOME)
    email_send_form = EmailForm()

    message = ""
    if request.method == "POST":
        email_send_form = EmailForm(request.POST)
        if email_send_form.is_valid():
            email = email_send_form.cleaned_data[AuthenticationFields.EMAIL]
            forget_password_log = AuditTrail.objects.create_log(user = str(email),
                                                                event_title = "Reseting password",
                                                                event_description = str(email)
                                                                                    + "  tryed to reset password")

            try:
                user = User.objects.get(email=email)
                subject = "Password Reset Requested"
                email_template = "accounts/password/password_reset_email.html"
                message = send_invitation(subject, email, render_to_string(email_template, {'hash': encrypt_id(user.id) }))
            except ObjectDoesNotExist:
                message = "Email not valid"
                forget_password_log = AuditTrail.objects.create_log(user=str(email),
                                                                    event_title="Unsuccessful attempt of reseting password",
                                                                    event_description=str(email)
                                                                                      + "  have unsuccessful attempt of resetnig password")
            forget_password_log.save()

    context = {
        General.MESSAGE: message,
        AuthenticationFields.EMAIL_SEND_FORM: email_send_form,
    }

    return render(request, "accounts/login.html", context)
