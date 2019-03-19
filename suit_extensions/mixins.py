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


class OperationModelAdminMixin(object):
    list_display_links = None
    edit_text = _("Change")
    delete_text = _("Delete")
    operation_text = _("Operations")

    def get_operations(self, obj):
        edit_link = """<a href="{edit_url}">{edit_text}</a>""".format(
            edit_url=reverse("admin:auth_user_change", args=(obj.pk,)),
            edit_text=self.edit_text
        )
        delete_link = """<a href="{delete_url}" class="text-error">{delete_text}</a>""".format(
            delete_url=reverse("admin:auth_user_delete", args=(obj.pk,)),
            delete_text=self.delete_text
        )
        operations = "{edit_link}&nbsp&nbsp&nbsp&nbsp{delete_link}".format(
            edit_link=edit_link, delete_link=delete_link
        )
        return mark_safe(operations)

    def get_list_display(self, request):
        self.get_operations.short_description = self.operation_text
        list_display = super(OperationModelAdminMixin, self).get_list_display(request)
        list_display += ("get_operations",)
        return list_display
