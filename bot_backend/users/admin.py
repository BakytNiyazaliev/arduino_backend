from django.contrib import admin

from .models import CustomerProfile, User, Session
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name', 'last_name', 'role', 'rfid']
    list_filter = ['role']


@admin.register(CustomerProfile)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["user", "points", "phone_number"]

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ["date", "customer", "points",]