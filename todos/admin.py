from django.contrib import admin

from .models import Todo
from .models import Team

admin.site.register(Todo)
admin.site.register(Team)