from django.contrib.admin.actions import delete_selected as _delete_selected
from django.utils.translation import ugettext_lazy as _


def delete_selected(*args, **kwargs):
    return _delete_selected(*args, **kwargs)


delete_selected.short_description = _("Delete selected items")
