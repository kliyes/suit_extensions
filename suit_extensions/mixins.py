from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.utils.safestring import mark_safe

from .actions import delete_selected


class ExtensionModelAdminMixin(object):
    change_form_template = "change_form.html"
    change_list_template = "change_list.html"
    delete_confirmation_template = "delete_confirmation.html"
    delete_selected_confirmation_template = "delete_selected_confirmation.html"
    object_history_template = "object_history.html"
    actions = [delete_selected]


class ExtensionModelAdmin(ExtensionModelAdminMixin, admin.ModelAdmin):
    pass


class OperationModelAdminMixin(object):
    list_display_links = None
    operations_list = ("get_change_operation", "get_delete_operation")

    def get_change_operation(self, obj):
        return """<a href="{change_url}">{change_text}</a>""".format(
            change_url=reverse(
                "admin:{app_label}_{model_name}_change".format(
                    app_label=obj._meta.app_label,
                    model_name=obj._meta.model_name
                ),
                args=(obj.pk,)
            ),
            change_text=_("Change")
        )

    def get_delete_operation(self, obj):
        return """<a href="{delete_url}" class="text-error">{delete_text}</a>""".format(
            delete_url=reverse(
                "admin:{app_label}_{model_name}_delete".format(
                    app_label=obj._meta.app_label,
                    model_name=obj._meta.model_name
                ),
                args=(obj.pk,)
            ),
            delete_text=_("Delete")
        )

    def get_operations_list(self):
        return self.operations_list

    def get_operations(self, obj):
        operations = []
        for operation in self.get_operations_list():
            operation_func = getattr(self, operation, None)
            if operation_func:
                operations.append(operation_func(obj))
        return mark_safe("&nbsp&nbsp&nbsp&nbsp".join(operations))
    get_operations.short_description = _("Operations")

    def get_list_display(self, request):
        list_display = super(OperationModelAdminMixin, self).get_list_display(request)
        list_display += ("get_operations",)
        return list_display


class OperationModelAdmin(OperationModelAdminMixin, admin.ModelAdmin):
    pass
