from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class OnlyLettersValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is not None:
            self.__message = value
        else:
            self.__message = "Your name must contain letters only!"

    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError(self.message)

@deconstructible
class MaxDigitsValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is not None:
            self.__message = value
        else:
            self.__message = "Your passcode must be exactly 6 digits!"

    def __call__(self, value):
        if len(value) != 6:
            raise ValidationError(self.message)