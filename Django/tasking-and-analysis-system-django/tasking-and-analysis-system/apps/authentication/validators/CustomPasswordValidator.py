import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}\`~!@#$%^&*_\-+=;:,./?]', password):
            raise ValidationError(
                ("The password must contain at least 1 of this symbols: " +
                 "()[\]{}\`~!@#$%^&*_\-+=;:,./?"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 of this symbols: " +
            "()[\]{}\`~!@#$%^&*_\-+=;:,./?"
        )
