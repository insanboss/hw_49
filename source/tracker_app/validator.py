from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class BadWordsValidation(BaseValidator):
    message = 'Value "%(value)s" is  inadmissible word , pls don`t write such words   '
    code = 'bad_word'

    def compare(self, a:str, b):
        a=a.split(' ')
        for i in a:
            if i.lower() in b:
                return True


def capital_letter(string:str):
        if string[0].upper()!=string[0]:
            raise ValidationError('First letter  is not capital, pls write first capital word')


@deconstructible
class MinLengthValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, a, b):
        return a < b

    def clean(self, x):
        return len(x)

