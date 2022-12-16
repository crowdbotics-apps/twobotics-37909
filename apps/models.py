from django.db import models
from django.conf import settings

class App(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=())
    framework = models.CharField(max_length=50, choices=())
    domain_name = models.CharField(max_length=50)
    screenshot = models.ImageField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Plan(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, related_name='sub_plan', on_delete=models.CASCADE)
    app = models.ForeignKey(App, related_name='sub_app', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)