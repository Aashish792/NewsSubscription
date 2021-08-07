from django.db import models

# Create your models here.

class Subscription(models.Model):
    subscription_emails = models.EmailField()
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100,default=None)

    def __str__(self):
        return self.subscription_emails

