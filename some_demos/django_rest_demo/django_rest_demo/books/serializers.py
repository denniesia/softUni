from rest_framework import serializers
from .models import Book

#Similar Syntax to ModelForms
# class BookForm(forms.ModelForm):
#     class Meta:
#         fields = '__all__'
#         model = Book



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Book