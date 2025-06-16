from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

@deconstructible
class CapitalizeFirstNameValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__mesage

    @message.setter
    def message(self, value):
        if value is not None:
            self.__message = value
        else:
            self.message = "Name must start with a capital letter!"

    def __call__(self, value):
        if value[0] != value[0].upper():
            return ValidationError(self.message)
