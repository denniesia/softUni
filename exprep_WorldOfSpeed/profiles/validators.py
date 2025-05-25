from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
from django.utils.text import slugify
@deconstructible
class CustomMinCharValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Username must be at least 3 chars long!"
        else:
            self.__message = value

    def __call__(self, value):
        if len(value) < 3:
            raise ValidationError(self.message)


@deconstructible
class AlphaNumericandUnderscoreValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Username must contain only letters, digits, and underscores!"
        else:
            self.__message = value

    def __call__(self, value):
        if value.lower() != slugify(value):
            raise ValidationError(self.message)
