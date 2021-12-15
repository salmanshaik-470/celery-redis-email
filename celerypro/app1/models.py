from django.db import models

# # Create your models here.
class Send_mail(models.Model):
    email = models.EmailField()
    msg=models.TextField()

