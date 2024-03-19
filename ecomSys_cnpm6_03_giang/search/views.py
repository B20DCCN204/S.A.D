from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from book.models import Book
from book.serializers import BookSerializer

class SearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('q', '')
        if query:
            books = Book.objects.filter(title__icontains=query).order_by('title')
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "Please provide a search query"}, status=status.HTTP_400_BAD_REQUEST)
