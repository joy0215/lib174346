from django.shortcuts import render
from mysite.models import Post, Comment , Book ,BorrowingHistor2
from django.http import HttpResponse , HttpResponseRedirect
from datetime import datetime
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q

# Create your views here.
def homepage(request):
    posts=Post.objects.all()
    now=datetime.now()
    return render(request,"index.html",locals())

def showpost(request,slug):
    try:
        post =Post.objects.get(slug=slug)
        if post !=None:
            return render(request, "post.html",locals())
        else:
            return redirect("/")
    except:
        return redirect("/")
    
def show_all_posts(request):
    posts = Post.objects.all()
    return render(request, 'allposts.html', locals())


def book_list(request):
    books = Post.objects.all()
    return render(request, 'book_list.html', {'books': books})



def borrow_book(request, book_id):
    #book = get_object_or_404(Book, pk=book_id)
    book = Post.objects.get(id=book_id)
        
    #borrower_name = request.POST.get('borrower_name')

    if not book.isBorrow:
        # 更新書籍狀態
        book.isBorrow = True
        book.save()

        # 創建借還書紀錄
        BorrowingHistor2.objects.create(
                book=book,
                date=timezone.now()
            ).save()
        
            
    return redirect('/book_list')



def return_book(request, book_id):
    #book = get_object_or_404(Book, pk=book_id)
    book = Post.objects.get(id=book_id)

    if book.isBorrow:
        book.isBorrow = False
        book.save()
        
        BorrowingHistor2.objects.create(
            book=book,
            date=timezone.now()
        ).save()

    return redirect('/book_list')



def show_comments(request, post_id):
    #comments = Comment.objects.filter(post=post_id)
    comments = Post.objects.get(id=post_id).comment_set.all()
    return render(request, 'comments.html', locals())



def new_post(request):
    print(f'form method: {request.method}')
    if request.method == 'GET':
        return render(request, 'myform_1.html', locals())
    elif request.method == 'POST':
        title = request.POST['title']
        slug = request.POST['slug']
        content = request.POST['content']
        category = request.POST.getlist('category')
        post = Post(title=title, slug=slug, body=content, category=category)
        post.save()
        return render(request, 'myform_1.html', locals())
    


def book_details(request):
    # 獲取所有的 BorrowingHistor2 記錄
    borrowing_history = BorrowingHistor2.objects.all()

    return render(request, 'book_details.html', {'BorrowingHistor2s': borrowing_history})



def book_search(request):
    query = request.GET.get('query', '')  # 如果未提供搜尋條件，預設為空字串
    posts = []

    if query:
        # 只有在搜尋詞存在時才進行查詢
        posts = Post.objects.filter(title__icontains=query)

    context = {'posts': posts, 'query': query}
    return render(request, 'book_search.html', context)
