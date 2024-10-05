from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Book, Author, Category, IssuedBook
from django.contrib.auth.models import User
from .forms import BookForm
from .models import Book, Author, Category, IssuedBook
from django.contrib.auth import authenticate, login


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



@login_required
def books_list(request):
    books = Book.objects.all()
    return render(request, 'library/books_list.html', {'books': books})



def login_view(request):
    # Your login logic
    return render(request, 'library/login.html')

def signup_view(request):
    # Your signup logic
    return render(request, 'library/signup.html')

def dashboard_view(request):
    # Your dashboard logic
    return render(request, 'library/dashboard.html')
# Create your views here.

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect based on user type
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
    # If GET request, show login form
    return render(request, 'your_folder/login.html')