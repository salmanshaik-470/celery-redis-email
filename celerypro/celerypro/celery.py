from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','celerypro.settings')

app=Celery('celerypro')
app.conf.enable_utc=False

app.conf.update(timezone='Asia/kolkata')

app.config_from_object(settings,namespace='CELERY')

# celery beat settings
app.conf.beat_schedule = {
    'send-mail-every-day': {
        'task': 'app1.tasks.send_mail_func',
        'schedule': crontab(minute=1)#, day_of_month=19, month_of_year=6),
        # 'args': (2,)
    }

}
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')