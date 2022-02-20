from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views import View

from Biblioteczka_app.forms import AddBookForm
from Biblioteczka_app.models import Author, Book


class Index(View):
    def get(self, request):
        return render(request, 'Index.html')


class AuthorAddView(View):
    def get(self, request):
        return render(request, 'add_author.html')

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Author.objects.create(first_name=first_name, last_name=last_name)
        return redirect(reverse('add_author'))


class AuthorListView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'author_list.html', {'authors': authors})


class AuthorDetailsView(View):
    def get(self, request, id):
        author = Author.objects.get(id=id)
        return render(request, 'details_author.html', {'author': author})


class AddBook(View):
    def get(self, request):
        form = AddBookForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddBookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            year = form.cleaned_data.get('year')
            author = form.cleaned_data.get('author')
            Book.objects.create(title=title, year=year, author=author)
            return redirect('add_book')
        return render(request, 'form.html', {'form': form})
