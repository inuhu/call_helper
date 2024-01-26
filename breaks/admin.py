from django.contrib import admin
from django.contrib.admin import TabularInline

from breaks.models.organizations import Organization
from breaks.models.groups import Group
from breaks.models.replacements import *
from breaks.models.dicts import *
from breaks.models.breaks import *

class ReplacementEmployeeInline(TabularInline):
    model = ReplacementEmployee
    fields = ('employee', 'status')


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'min_active')


@admin.register(Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'date', 'break_start', 'break_end', 'break_max_duration')
    inlines = (ReplacementEmployeeInline,)

@admin.register(ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active')

@admin.register(BreakStatus)
class BreakStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active')

@admin.register(Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = ('id', 'replacement', 'employee', 'break_start', 'break_end')
