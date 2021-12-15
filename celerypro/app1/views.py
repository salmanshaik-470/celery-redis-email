from django.shortcuts import render
from .tasks import test_func
from django.http import HttpResponse
from .tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
from .models import Send_mail

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("<h1>hai loop is done</h1>")


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Senjt")


def schedule_mail(request):
    if request.method == "POST":
        schedule, created = CrontabSchedule.objects.get_or_create(hour=request.POST.get('Hrs'),
                                                                  minute=request.POST.get('Min'))
        task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_" + request.POST.get('Min'),
                                           task='app1.tasks.send_mail_func')  # , args = json.dumps([[2,3]]))
        Send_mail.objects.create(email=request.POST.get('email'),msg=request.POST.get('msg'))
        return HttpResponse("Done")
    return render(request,'sendmail.html')

