from django.contrib import admin

# Register your models here.

from .models import Room,Table,Menu

admin.site.register(Room)
admin.site.register(Table)
admin.site.register(Menu)
