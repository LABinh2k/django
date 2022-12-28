from django.contrib import admin

from .models import Team, Character
# Register your models here.

admin.site.register([Team, Character])