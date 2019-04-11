from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from .models import Publisher, Author, Book
from django.http import HttpResponse


def index(request):
    context = {}
    this_book = Book.objects.get(id=1)
    # همه ی نویسندگان یک کتاب را نمایش بده
    this_authors = this_book.authors.all
    context['view_book_authors'] = this_authors
    # اسم کتاب را نمایش بده
    this_title_book = this_book.title
    context['view_title_book'] = this_title_book
    # وب سایت ناشر کتاب را نشان بده
    this_website_publisher = this_book.publisher.website
    context['view_website_publisher'] = this_website_publisher
    # همه ی کتاب های یک ناشر را نشان بده
    this_publisher = Publisher.objects.get(id=1)
    this_publisher_books = this_publisher.book_set.all
    context['view_publisher_books'] = this_publisher_books
    # یک نویسنده چند تا کتاب مختلف تولید کرده؟
    this_author = Author.objects.get(id=1)
    this_authors_books = this_author.book_set.all
    context['view_author_books'] = this_authors_books
    return render(request, 'index.html', context)
