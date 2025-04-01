from django.db import models

# Create your models here.

class Item(models.Model):
    STATUS_CHOICES = [
        ('Lost', 'Lost'),
        ('Found', 'Found'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=5, choices=STATUS_CHOICES)
    date_reported = models.DateField(auto_now_add=True)
    contact_info = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name} ({self.status})"
