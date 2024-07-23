
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_report_email(recipient_email, subject, message):
    send_mail(
        subject,
        message,
        'bayaman2101@gmail.com',
        [recipient_email],
        fail_silently=False,
    )
