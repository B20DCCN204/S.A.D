from decimal import Decimal
from django.db import models
from book.models import Book
from django.contrib.auth.models import User
class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)
    book_id = models.IntegerField(default=-1)
    class Meta:
        db_table = 'carts'
        ordering = ['date_added']
    def get_book(self):
        try:
            book = Book.objects.using('mongodb').get(id=self.book_id)
            return book
        except Book.DoesNotExist:
            return None
    @property
    def total(self):
        book = self.get_book()
        price_decimal = Decimal(str(book.price))
        return self.quantity * price_decimal
    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()

    def __str__(self):
        book = self.get_book()
        if book:
            return book.title
        else:
            return "Unknown Book"
