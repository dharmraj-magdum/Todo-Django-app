from django.contrib import admin
from .models import Todo
# Register your models here.
admin.site.disable_action("delete_selected")
admin.site.register(Todo)
