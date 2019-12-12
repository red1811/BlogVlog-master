from django.contrib import admin

# Register your models here.
from accounts.models import LoginValue

admin.site.register(LoginValue)