from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated


class CartList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        carts = Cart.objects.filter(owner=request.user)
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)


class AddToCart(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            book_id = serializer.validated_data['book_id']
            quantity = serializer.validated_data['quantity']
            try:
                cart = Cart.objects.get(owner=request.user, book_id=book_id)
                cart.augment_quantity(quantity)
                serializer = CartSerializer(cart)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Cart.DoesNotExist:
                serializer.save(owner=request.user)  # Lưu owner khi tạo mới cart
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteCart(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk, owner=request.user)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cart.delete()
        return Response({"message": "Delete cart successfully!!!"},status=status.HTTP_204_NO_CONTENT)



