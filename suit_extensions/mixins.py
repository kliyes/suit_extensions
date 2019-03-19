from .actions import delete_selected


class ExtensionModelAdminMixin(object):
    change_form_template = "change_form.html"
    change_list_template = "change_list.html"
    delete_confirmation_template = "delete_confirmation.html"
    delete_selected_confirmation_template = "delete_selected_confirmation.html"
    object_history_template = "object_history.html"
    actions = [delete_selected]
