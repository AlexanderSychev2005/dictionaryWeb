from django.contrib import admin
from translation.models import Translation


# Register your models here.
@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('text',)}),
        ('Source word', {'fields': ('source_word',)}),
        ('Target language', {'fields': ('target_language',)}),
    )
