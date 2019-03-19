from django.utils.translation import ugettext_lazy as _
from django import forms
from django.conf import settings
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget

from suit.widgets import SuitSplitDateTimeWidget, SuitDateWidget, \
    SuitTimeWidget


def _make_attrs(attrs, defaults=None, classes=None):
    result = defaults.copy() if defaults else {}
    if attrs:
        result.update(attrs)
    if classes:
        result["class"] = " ".join((classes, result.get("class", "")))
    return result


class ExtendedSuitSplitDateTimeWidget(SuitSplitDateTimeWidget):
    """
    Extend SuitSplitDateTimeWidget so that we can apply different attrs on SuitDateWidget and SuitTimeWidget
    """
    def __init__(self, attrs=None, date_attrs=None, date_format=None,
                 time_attrs=None, time_format=None):
        widgets = [
            SuitDateWidget(attrs=date_attrs, format=date_format),
            SuitTimeWidget(attrs=time_attrs, format=time_format)
        ]
        forms.MultiWidget.__init__(self, widgets, attrs)


class DatePickerWidget(AdminDateWidget):
    def __init__(self, attrs=None, datepicker_options=None, format=None):
        default_datepicker_options = {
            "todayBtn": "linked",
            "todayHighlight": 1,
            "format": "yyyy-mm-dd",
            "autoclose": 1,
            "language": "zh-CN",
            "calendarWeeks": 1
        }
        if datepicker_options:
            default_datepicker_options.update(datepicker_options)

        defaults = {
            "placeholder": _('Date:')[:-1],
            "datepicker": 1,
            "data-datepicker-options": default_datepicker_options
        }
        new_attrs = _make_attrs(attrs, defaults, "vDateField input-small")
        super(DatePickerWidget, self).__init__(attrs=new_attrs, format=format)

    @property
    def media(self):
        extra = '' if settings.DEBUG else '.min'
        js = [
            'vendor/jquery/jquery%s.js' % extra,
            'jquery.init.js',
            'calendar.js'
        ]
        return forms.Media(
            js=["admin/js/%s" % path for path in js] +
               [
                   "suit_extensions/base/js/DateTimeShortcuts.js",
                   "suit_extensions/bootstrap-datepicker/js/bootstrap-datepicker.min.js",
                   "suit_extensions/bootstrap-datepicker/locales/bootstrap-datepicker.zh-CN.min.js",
                   "suit_extensions/base/js/datepicker_init.js"
               ],
            css={
                "all": (
                    "suit_extensions/bootstrap-datepicker/css/bootstrap-datepicker.min.css",
                )
            }
        )


class TimePickerWidget(AdminTimeWidget):
    def __init__(self, attrs=None, timepicker_options=None, format=None):
        default_timepicker_options = {
            "showSeconds": 1,
            "showMeridian": 0,
            "showInputs": 0,
            "defaultTime": 0,
            "icons": {
                "up": 'icon-chevron-up',
                "down": 'icon-chevron-down'
            }
        }
        if timepicker_options:
            default_timepicker_options.update(timepicker_options)

        defaults = {
            "placeholder": _('Time:')[:-1],
            "timepicker": 1,
            "data-timepicker-options": default_timepicker_options
        }
        new_attrs = _make_attrs(attrs, defaults, "vTimeField input-small")
        super(TimePickerWidget, self).__init__(attrs=new_attrs, format=format)

    @property
    def media(self):
        extra = '' if settings.DEBUG else '.min'
        js = [
            'vendor/jquery/jquery%s.js' % extra,
            'jquery.init.js',
            'calendar.js',
        ]
        return forms.Media(
            js=["admin/js/%s" % path for path in js] +
               [
                   "suit_extensions/base/js/DateTimeShortcuts.js",
                   "suit_extensions/bootstrap-timepicker/js/bootstrap-timepicker.min.js",
                   "suit_extensions/base/js/timepicker_init.js"
               ],
            css={
                "all": (
                    "suit_extensions/bootstrap-timepicker/css/bootstrap-timepicker.min.css",
                )
            }
        )


class DateTimePickerWidget(forms.SplitDateTimeWidget):
    """
    Use bootstrap-datepicker and bootstrap-timepicker
    """
    def __init__(self, attrs=None, datepicker_options=None, timepicker_options=None):
        widgets = [
            DatePickerWidget(attrs=attrs, datepicker_options=datepicker_options),
            TimePickerWidget(attrs=attrs, timepicker_options=timepicker_options)
        ]
        forms.MultiWidget.__init__(self, widgets, attrs)
