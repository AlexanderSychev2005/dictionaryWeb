from django.contrib import admin
from .models import Dictionary

class WordInline(admin.TabularInline):
    model = Dictionary.words.through

# Register your models here.
@admin.register(Dictionary)
class DictionaryAdmin(admin.ModelAdmin):
    list_filter = ('name','source_language', 'target_language',)
    list_display = ('id', 'name', 'source_language', 'target_language',)
    search_fields = ('name', 'source_language', 'target_language',)
    list_display_links = ('id', 'name',)
    inlines = [WordInline]
    fieldsets = (
        (None, {'fields': ('name',)}),
        ('Description', {'fields': ('description',)}),
        ('Languages', {'fields': ('source_language', 'target_language',)}),
    )
    ordering = ('id',)


