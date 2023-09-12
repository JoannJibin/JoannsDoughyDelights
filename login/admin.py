from django.contrib import admin

# Register your models here.
from .models import login
class LoginAdmin(admin.ModelAdmin):
 None
admin.site.register(login, LoginAdmin)
