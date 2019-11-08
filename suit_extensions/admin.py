from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group

from .mixins import ExtensionModelAdminMixin


UserModel = get_user_model()


class ExtendedUserAdmin(ExtensionModelAdminMixin, UserAdmin):
    pass


class ExtendedGroupAdmin(ExtensionModelAdminMixin, GroupAdmin):
    pass


admin.site.unregister(UserModel)  # unregister default admin first
admin.site.unregister(Group)  # unregister default admin first

admin.site.register(UserModel, ExtendedUserAdmin)
admin.site.register(Group, ExtendedGroupAdmin)
