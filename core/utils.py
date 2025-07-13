from django.core.mail import send_mail

def send_notification_email(to_email, subject, message):
    send_mail(
        subject,
        message,
        None,  # uses DEFAULT_FROM_EMAIL from settings
        [to_email],
        fail_silently=False,
    )
