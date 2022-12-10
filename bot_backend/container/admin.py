from django.contrib import admin


from .models import Container, Report

@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_green', 'full_red', 'full_blue']
    list_filter = ['full_green', 'full_red', 'full_blue']

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'container', 'date']
    list_filter = ['container', 'date']