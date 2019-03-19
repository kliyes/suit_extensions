from django import template
from django.http import HttpRequest

from suit import utils
from suit.templatetags.suit_menu import get_admin_site, Menu

django_version = utils.django_major_version()
register = template.Library()

if django_version < (1, 9):
    simple_tag = register.assignment_tag
else:
    simple_tag = register.simple_tag


@simple_tag(takes_context=True)
def get_menu_compat(context, request):
    """
    :type request: HttpRequest
    """
    if not isinstance(request, HttpRequest):
        return None

    # Try to get app list
    if hasattr(request, 'current_app'):
        # Django 1.8 uses request.current_app instead of context.current_app
        template_response = get_admin_site(request.current_app).index(request)
    else:
        try:
            template_response = get_admin_site(context.current_app).index(request)
        # Django 1.10 removed the current_app parameter for some classes and functions.
        # Check the release notes.
        except AttributeError:
            template_response = get_admin_site(context.request.resolver_match.namespace).index(request)

    try:
        app_list = template_response.context_data['app_list']
    except Exception:
        return

    return MenuCompat(context, request, app_list).get_app_list()


class MenuCompat(Menu):

    def fill_keys(self, dict, keys):
        for key in keys:
            if key not in dict:
                if key == "is_active":
                    dict[key] = False
                else:
                    dict[key] = None
