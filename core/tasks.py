from celery import shared_task
from .email_templates import TEMPLATES
from django.core.mail import send_mail

@shared_task
def send_notification_email_task(to, notification_type, context):
    template = TEMPLATES.get(notification_type)
    if not template:
        raise ValueError(f"No template found for {notification_type}")

    subject = template["subject"].format(**context)
    message = template["body"].format(**context)

    send_mail(subject, message, "airline.booking.backend.email@gmail.com", [to])
