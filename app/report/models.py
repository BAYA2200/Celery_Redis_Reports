from django.db import models

# Create your models here.


# class Report(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_requests')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     report_file = models.FileField(upload_to='reports/', null=True, blank=True)
#     recipient_email = models.EmailField()
# models.py

from django.db import models

class Report(models.Model):
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Report to {self.recipient_email}'

