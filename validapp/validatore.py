
import re

from django.core.exceptions import ValidationError
import re


def Validate_age(value):

    age = int(value)

    if age >= 18:
        return value
    else:
        raise ValidationError("this field takes 18years minimum .")


