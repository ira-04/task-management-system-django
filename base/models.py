from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # deadline = models.DateTimeField(null=True, blank=True)  
    # PRIORITY_CHOICES = [
    #     ('LOW', 'Low'),
    #     ('MEDIUM', 'Medium'),
    #     ('HIGH', 'High'),
    # ]
    # priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM')  
    # deadline = models.DateTimeField()
    deadline = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=1))  # Set default to one day from now
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')
    # done = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
