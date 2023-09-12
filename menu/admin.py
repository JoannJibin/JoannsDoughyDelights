from django.contrib import admin

# Register your models here.
from .models import menu
class menuAdmin(admin.ModelAdmin):
    list_display= ('Name','Description','Price')
admin.site.register(menu,menuAdmin)