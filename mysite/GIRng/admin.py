from django.contrib import admin

from .models import Team, Character, NormalAttack, ElementalSkill, \
    ElementalBurst, Passive, Artifact, Weapon, Constellation
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    actions = ['setEmpty']

    @admin.action(description="team")
    def setEmpty(self, request, queryset):
        pass


admin.site.register(
    [Team, Character, NormalAttack, ElementalSkill,
     ElementalBurst, Passive, Artifact, Weapon, Constellation],
    TeamAdmin)
