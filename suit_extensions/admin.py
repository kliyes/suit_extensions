from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .mixins import ExtensionModelAdminMixin


UserModel = get_user_model()


class ExtendedUserAdmin(ExtensionModelAdminMixin, BaseUserAdmin):
    pass


admin.site.unregister(UserModel)  # unregister default admin first
admin.site.register(UserModel, ExtendedUserAdmin)
