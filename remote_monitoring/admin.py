from django.contrib import admin
from .models import Machine, Email,UserMetrics


# Register your models here.

admin.site.register(Machine)
admin.site.register(Email)
admin.site.register(UserMetrics)

