#
# # from .models import Send_mail
# from django.contrib.auth import get_user_model
from celery import shared_task
# from django.core.mail import send_mail
# from celerypro import settings
# from django.utils import timezone
# from datetime import timedelta
# import time
#

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print(i)
    return "Done"
#
# @shared_task(bind=True)
# def send_mail_func(self):
#     users = get_user_model().objects.all()
#     #timezone.localtime(users.date_time) + timedelta(days=2)
#     for user in users:
#         mail_subject = "Hi! Celery Testing"
#         message = "If you are liking my content, please hit the like button and do subscribe to my channel"
#         to_email = user.email
#         send_mail(
#             subject = mail_subject,
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[to_email],
#             fail_silently=False,
#         )
#     return "Done"
#
# # @shared_task
# # def send_email(email_id, message):
# #     time.sleep(10)
# #     print(f"Email is sent to {email_id}. Message sent was - {message}")

from django.contrib.auth import get_user_model

from celery import shared_task
from django.core.mail import send_mail
from celerypro import settings

@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "welcome to the celery, sending email through salman "
        to_email = "salmanshaik73@gmail.com"
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"