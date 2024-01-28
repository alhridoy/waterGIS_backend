from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError("The password must contain at least 1 uppercase letter, A-Z.")
        if not re.findall('[a-z]', password):
            raise ValidationError("The password must contain at least 1 lowercase letter, a-z.")
        if not re.findall('[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError("The password must contain at least 1 symbol: " + 
                                  "!@#$%^&*(),.?\":{}|<>")

    def get_help_text(self):
        return "Your password must contain at least 1 uppercase letter, A-Z, " + \
               "1 lowercase letter, a-z, and 1 symbol: !@#$%^&*(),.?\":{}|<>"