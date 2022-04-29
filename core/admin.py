from csv import list_dialects
from django.contrib import admin
from core.models import Idea

# Register your models here.
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    list_filter = ('title',)

admin.site.register(Idea, IdeaAdmin)