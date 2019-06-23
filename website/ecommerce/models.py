from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Otp_Generate(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    otp = models.PositiveIntegerField(default=0)
    def __str__(self):
         return ("%s" %(self.otp))




