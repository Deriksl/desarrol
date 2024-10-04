from django.contrib import admin
from .models import Task
from .models import Country, State


class taskadmin(admin.ModelAdmin):
    readonly_fields = ('created', )

# Register your models here.

admin.site.register(Task, taskadmin)
admin.site.register(Country)
admin.site.register(State)