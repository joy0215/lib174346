"""
URL configuration for mblog0927 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path , include
from mysite import views as mv
from mysite.views import book_list, borrow_book, return_book
from mytest import views as testv

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",mv.homepage, name="homepage"),
    path("post/<slug:slug>/",mv.showpost,name="showpost"),
    path('book_list/', book_list, name='book_list'),
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('return/<int:book_id>/', return_book, name='return_book'),
    path('post/', mv.show_all_posts, name="show-all-posts"),
    path('post/<int:post_id>/comments', mv.show_comments, name='show-comments'),
    path('post/new', mv.new_post, name="post-new"),
    path('test/', testv.index, name="test-new"),
    path('test/delpost/<int:pid>/', testv.delpost),
    path('test/contact', testv.contact),
    path('post2db/', testv.post2db),
    path('register/', testv.register),
    path('login/', testv.login, name='login'),
    path('profile/', testv.profile),
    path('borrow/<int:id>/', borrow_book, name='borrow_book'),
    path('book_details/', testv.book_details),
    

]
