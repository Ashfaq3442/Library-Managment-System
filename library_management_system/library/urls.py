from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-book/', views.add_book, name='add_book'),
    path('books/', views.books_list, name='books_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/',custom_login , name='login'),



]
