from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import send_notification_email_task


class TestEmailView(APIView):
    def post(self, request):
        to = request.data.get("to")
        subject = request.data.get("subject")
        message = request.data.get("message")

        if not all([to, subject, message]):
            return Response({"error": "Missing fields"}, status=400)

        send_notification_email_task.delay(to, subject, message)

        return Response({"message": "Email task queued successfully"})
    
class SendNotificationEmailView(APIView):
    def post(self, request):
        print("📥 Incoming request to /api/send-email/:", request.data)

        to = request.data.get("to")
        notification_type = request.data.get("notification_type") or request.data.get("template_type")
        context = request.data.get("context", {})

        if not to or not notification_type:
            print("❌ Missing 'to' or 'notification_type/template_type'")
            return Response({"error": "Missing fields"}, status=status.HTTP_400_BAD_REQUEST)

        send_notification_email_task.delay(to, notification_type, context)
        return Response({"message": "Task queued successfully"})
