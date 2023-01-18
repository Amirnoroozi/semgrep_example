# cf. https://github.com/django/django/blob/ecaac9e42f497be04ddc72dfebb6e397ccca9517/django/
contrib/humanize/templatetags/humanize.py
import re
from datetime import date, datetime
from decimal import Decimal
from django import template
from django.template import defaultfilters
from django.utils.formats import number_format
from django.utils.safestring import mark_safe
from django.utils.timezone import is_aware, utc
from django.utils.translation import (
    gettext as _, gettext_lazy, ngettext, ngettext_lazy, npgettext_lazy,
    pgettext, round_away_from_one,
)
register = template.Library()
# ruleid:filter-with-is-safe
@register.filter(is_safe=True)
def ordinal(value):
    """
    Convert an integer to its ordinal as a string. 1 is '1st', 2 is '2nd',
    3 is '3rd', etc. Works for any integer.
    try:
        value = int(value)
    except (TypeError, ValueError):
        return value
    if value % 100 in (11, 12, 13):
        # Translators: Ordinal format for 11 (11th), 12 (12th), and 13 (13th).
        value = pgettext('ordinal 11, 12, 13', '{}th').format(value)
    else:
        templates = (
            # Translators: Ordinal format when value ends with 0, e.g. 80th.
            pgettext('ordinal 0', '{}th'),
            # Translators: Ordinal format when value ends with 1, e.g. 81st, except 11.
            pgettext('ordinal 1', '{}st'),
            # Translators: Ordinal format when value ends with 2, e.g. 82nd, except 12.
            pgettext('ordinal 2', '{}nd'),
            # Translators: Ordinal format when value ends with 3, e.g. 83th, except 13.
            pgettext('ordinal 3', '{}rd'),
            # Translators: Ordinal format when value ends with 4, e.g. 84th.
            pgettext('ordinal 4', '{}th'),
            # Translators: Ordinal format when value ends with 5, e.g. 85th.
            pgettext('ordinal 5', '{}th'),
            # Translators: Ordinal format when value ends with 6, e.g. 86th.
            pgettext('ordinal 6', '{}th'),
            # Translators: Ordinal format when value ends with 7, e.g. 87th.
            pgettext('ordinal 7', '{}th'),
            # Translators: Ordinal format when value ends with 8, e.g. 88th.
            pgettext('ordinal 8', '{}th'),
            # Translators: Ordinal format when value ends with 9, e.g. 89th.
            pgettext('ordinal 9', '{}th'),
        )
        value = templates[value % 10].format(value)
    # Mark value safe so i18n does not break with <sup> or <sub> see #19988
    return mark_safe(value)
def intcomma(value, use_l10n=True):
    Convert an integer to a string containing commas every three digits.
    For example, 3000 becomes '3,000' and 45000 becomes '45,000'.
    if use_l10n:
        try:
            if not isinstance(value, (float, Decimal)):
                value = int(value)
        except (TypeError, ValueError):
            return intcomma(value, False)
        else:
            return number_format(value, use_l10n=True, force_grouping=True)
    orig = str(value)
    new = re.sub(r"^(-?\d+)(\d{3})", r'\g<1>,\g<2>', orig)
    if orig == new:
        return new
        return intcomma(new, use_l10n)
# A tuple of standard large number to their converters
intword_converters = (
    (6, lambda number: ngettext('%(value)s million', '%(value)s million', number)),
    (9, lambda number: ngettext('%(value)s billion', '%(value)s billion', number)),
    (12, lambda number: ngettext('%(value)s trillion', '%(value)s trillion', number)),
    (15, lambda number: ngettext('%(value)s quadrillion', '%(value)s quadrillion', number)),
    (18, lambda number: ngettext('%(value)s quintillion', '%(value)s quintillion', number)),
    (21, lambda number: ngettext('%(value)s sextillion', '%(value)s sextillion', number)),
    (24, lambda number: ngettext('%(value)s septillion', '%(value)s septillion', number)),
    (27, lambda number: ngettext('%(value)s octillion', '%(value)s octillion', number)),
    (30, lambda number: ngettext('%(value)s nonillion', '%(value)s nonillion', number)),
    (33, lambda number: ngettext('%(value)s decillion', '%(value)s decillion', number)),
    (100, lambda number: ngettext('%(value)s googol', '%(value)s googol', number)),
# ok:filter-with-is-safe
@register.filter(is_safe=False)
def intword(value):
    Convert a large integer to a friendly text representation. Works best
    for numbers over 1 million. For example, 1000000 becomes '1.0 million',
    1200000 becomes '1.2 million' and '1200000000' becomes '1.2 billion'.
    abs_value = abs(value)
    if abs_value < 1000000:
