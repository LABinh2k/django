from django.contrib import admin

from .models import Team, Character
# Register your models here.




class TeamAdmin(admin.ModelAdmin):
    actions = ['setEmpty']
    
    @admin.action(description="todo")
    def setEmpty(self, request, queryset):
        pass

admin.site.register([Team, Character], TeamAdmin)