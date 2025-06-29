from django.shortcuts import render, get_object_or_404
from django_rest_demo.books.models import Book
from django.http import JsonResponse

from rest_framework.decorators import api_view
from django_rest_demo.books.serializers import BookSerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.utils.representation import serializer_repr
from rest_framework.views import APIView


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

@api_view(['GET', 'POST'])
def list_books_view(request):
    if request.method == 'GET':
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True) #books -> QuerySet, more than one object -> many=True

        return Response(serializer.data, status=status.HTTP_200_OK) # -> .data - data in JSON format

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK) #returning the created object

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #if the serializer is not valid



class ListBooksView(APIView): #APIView is the base view
    def get(self, request):
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)  # books -> QuerySet, more than one object -> many=True

        return Response(serializer.data, status=status.HTTP_200_OK)  # -> .data - data in JSON format

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  # returning the created object

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # if the serializer is not valid


# class ListBooksApiView(ListAPIView):  #generic ListView
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookViewSet(APIView):

    @staticmethod
    def get_object(pk):
        return get_object_or_404(Book, pk=pk)

    @staticmethod
    def serializer_valid(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk:int):
        book = self.get_object(pk)

        serializer = BookSerializer(book) #one object so no many=True
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk:int):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)

        return self.serializer_valid(serializer)

    def patch(self, request, pk:int):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data, partial=True) #method is patch thats why partial = True

        return self.serializer_valid(serializer)

    def delete(self, request, pk:int):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







