"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import HomeView
from book.views import BookView, AddBook, BookDetail, BookUpdate, BookDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('booklist/', BookView.as_view(), name='booklist'),
    path('addbook/', AddBook.as_view(), name='addbook'),
    path('bookdetail/<int:pk>', BookDetail.as_view(), name='bookdetail'),
    path('bookupdate/<int:pk>', BookUpdate.as_view(), name='bookupdate'),
    path('book/delete/<int:pk>', BookDelete.as_view(), name='bookdelete'),
]
