from django.urls import path

from . import views

urlpatterns = [
    path('', views.BooksListView.as_view()),
    path('<int:pk>/', views.BookDetailView.as_view()),
    path('<int:pk>/update/', views.BookUpdateView.as_view()),
    path('<int:pk>/delete/', views.BookDeleteView.as_view()),
    path('create/', views.BookCreateView.as_view()),
]
