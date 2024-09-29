from django.urls import path
from . import views # "." is relative import from last package, i.e. path from django.urls

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.BookListView.as_view(), name="books"),
    path("book/<int:pk>", views.BookDetailView.as_view(), name="book-detail"),
    path("authors/", views.AuthorListView.as_view(), name="authors"),
    path("author/<int:pk>", views.AuthorDetailView.as_view(), name="author-detail"),
]

urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

# aqdd admin page to see all borrowed books of users:
# urlpatterns += [
#     path('allbooks/', views.LoanedBooksByUserListView.as_view(), name='all-borrowed-books '),
# ]