from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from .models import Book
from django.urls import reverse_lazy

# Create your views here.

class BookView(ListView):
    model = Book

class AddBook(CreateView):
        model=Book
        fields=['title', 'author']

class BookDetail(DetailView):
    model =Book

class BookUpdate(UpdateView):
    model=Book
    fields=['title', 'author']

class BookDelete(DeleteView):
    model=Book
    success_url=reverse_lazy('booklist')
