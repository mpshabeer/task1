from django.contrib import admin

# Register your models here.
from .models import place, Team

admin.site.register(place)
admin.site.register(Team)