from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('list/',views.BookListView.as_view(),name='booklist'),
    path('detail/<int:pk>',views.BookDetailView.as_view(),name='bookdetail'),
    path('search/',views.search_book.as_view(),name='search'),
]