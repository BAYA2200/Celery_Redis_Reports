from django.urls import path
from .views import SendReportView

urlpatterns = [
    path('reports/', SendReportView.as_view(), name='report_post_api'),
]
