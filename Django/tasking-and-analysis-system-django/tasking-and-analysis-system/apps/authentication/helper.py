from django.core.mail import EmailMessage
from smtplib import SMTPException
from core.settings import EMAIL_HOST_USER
from apps.constants import FERNET, General
import datetime


def encrypt_id(user_id):
    final_date = datetime.datetime.now() + datetime.timedelta(minutes=15)
    encrypting_string = str(user_id) + "," + final_date.strftime(General.DATETIME_FORMAT)
    encrypted_string = FERNET.encrypt(encrypting_string.encode())
    return encrypted_string.decode()


def decrypt_id(encrypted_string):
    try:
        decrypted_string = FERNET.decrypt(encrypted_string.encode()).decode()
        user_id, final_date = decrypted_string.split(',')
        if datetime.datetime.now() <= datetime.datetime.strptime(final_date, General.DATETIME_FORMAT):
            return user_id
        else:
            return None
    except Exception:
        return None


def send_invitation(subject, email, email_template):
    try:
        message = EmailMessage(subject, email_template, EMAIL_HOST_USER, [email])
        message.content_subtype = 'html'
        message.send(fail_silently=False)
        return "Sent"
    except SMTPException:
        return "Can`t send"
