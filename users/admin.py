from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    readonly_fields = ['created_at', 'last_login']

    list_display = (
        'id', 'username', 'first_name', 'last_name', 'email', 'is_admin', 'is_active', 'is_staff', 'is_superuser', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'is_admin')

    list_display_links = ('id', 'first_name')

    date_hierarchy = "created_at"

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin')}),
        ('Some dates', {'fields': ('created_at', 'last_login')})

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'username', 'first_name', 'middle_name', 'last_name', 'is_active', 'is_staff',
                'is_superuser', 'is_admin')}
         ),
    )

    ordering = ('id',)
    filter_horizontal = ()