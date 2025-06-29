from django.shortcuts import render
from django_rest_demo.books.models import Book
from django.http import JsonResponse

from rest_framework.decorators import api_view
from django_rest_demo.books.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# Django View
# def list_books_view(request):
#     books = Book.objects.all()
#
#     context = {
#         'books' : books
#     }
#     return render(request, 'some_template.html', context)

# Option without the rest_framework
# This would raise a TypeError because the QuerySet must be converted, is not serializable

# def list_books_view(request):
#     books = Book.objects.all()
#     context = {
#         'books' : books
#      }
#     return JsonResponse(context) -> this expects string

@api_view(['GET'])
def list_books_view(request):
    books = Book.objects.all()

    serializer = BookSerializer(books, many=True) #books -> QuerySet, more than one object -> many=True

    return Response(serializer.data, status=status.HTTP_200_OK) # -> .data - data in JSON format


















