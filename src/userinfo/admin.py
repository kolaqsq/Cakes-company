from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserInfo


class UserInfoInline(admin.StackedInline):
    model = UserInfo
    can_delete = False
    # readonly_fields = ('image_tag',)


class UserAdmin(BaseUserAdmin):
    inlines = (UserInfoInline,)
    list_display = ('username', 'first_name', 'is_active')
    list_filter = ('groups',)
    autocomplete_fields = ('groups',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
