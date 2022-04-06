from django.db import models

from django.contrib.auth.models import User


# Books model which stores books data.
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    books_name = models.CharField(max_length=255, null=True, blank=False)
    books_description = models.CharField(max_length=255, null=True, blank=True)
    books_img=models.ImageField(upload_to='book/images/', default=None)
    def __str__(self):
         return str(self.books_name)
