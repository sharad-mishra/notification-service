from django.urls import path
from .views import SendNotificationEmailView

urlpatterns = [
    path('send-email/', SendNotificationEmailView.as_view()),
]
