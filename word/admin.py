from django.contrib import admin

from word.models import Word


# Register your models here.
class TranslationsInline(admin.TabularInline):
    model = Word.translations.through


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Word', {'fields': ('text',)}),
        ('Language', {'fields': ('language',)}),
    )
    inlines = [TranslationsInline]
