from django.db import models
from django.contrib import admin
class Book(models.Model):
    title=models.CharField(max_length=20);
    author_name=models.CharField(max_length=30);
    author_name=models.CharField(max_length=30);
    book_id=models.IntegerField();
    number_of_pages=models.IntegerField();
    year_of_publishing=models.DateField();
    book_price=models.IntegerField();
class BookAdmin(admin.ModelAdmin):
    list_display=("title","author_name","book_id","number_of_pages","year_of_publishing","book_price",);