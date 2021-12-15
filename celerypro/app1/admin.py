from django.contrib import admin
from .models import Send_mail
# Register your models here.
#
@admin.register(Send_mail)
class emailadmin(admin.ModelAdmin):
    list_display = ['email','msg']