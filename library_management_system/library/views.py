from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Book, Author, Category, IssuedBook
from django.contrib.auth.models import User
from .forms import BookForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'library/signup.html', {'form': form})




@login_required
def dashboard(request):
    users_count = User.objects.count()
    books_count = Book.objects.count()
    categories_count = Category.objects.count()
    issued_books_count = IssuedBook.objects.count()
    authors_count = Author.objects.count()
    return render(request, 'library/dashboard.html', {
        'users_count': users_count,
        'books_count': books_count,
        'categories_count': categories_count,
        'issued_books_count': issued_books_count,
        'authors_count': authors_count
    })



@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

# Create your views here.
