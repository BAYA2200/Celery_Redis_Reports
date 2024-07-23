
from .task import send_report_email

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReportSerializer

class SendReportView(APIView):
    def post(self, request):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            report = serializer.save()
            send_report_email.delay(report.recipient_email, report.subject, report.message)
            return Response({'status': 'Report is being sent'}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
