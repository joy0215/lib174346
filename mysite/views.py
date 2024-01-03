from django.shortcuts import render
from mysite.models import Post, Comment , Book ,BorrowingHistory
from django.http import HttpResponse , HttpResponseRedirect
from datetime import datetime
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse

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


'''def borrow_book(request, book_id):
    book = get_object_or_404(Post, id=book_id)

    if not book.isBorrow:
        book.isBorrow = True
        book.save()

    # 假設你有一個表單，其中包含借書人姓名等信息
    borrower_name = request.POST['borrower_name']

    if not book.is_borrowed:
        # 更新書籍狀態
        book.is_borrowed = True
        book.save()

        # 創建借還書紀錄
        BorrowingHistory.objects.create(
            book=book,
            borrower_name=borrower_name,
            borrowed_date=timezone.now()
        )

    return HttpResponseRedirect(reverse('book_detail', args=(book.id,))) '''


def borrow_book(request, book_id):
    #book = get_object_or_404(Book, pk=book_id)
    book = Post.objects.get(id=book_id)
        
    #borrower_name = request.POST.get('borrower_name')

    if not book.isBorrow:
        # 更新書籍狀態
        book.isBorrow = True
        book.save()

        # 創建借還書紀錄
        BorrowingHistory.objects.create(
                book=book,
                borrowed_date=timezone.now()
            ).save()
        
            
    return redirect('/book_list')



def return_book(request, book_id):
    #book = get_object_or_404(Book, pk=book_id)
    book = Post.objects.get(id=book_id)

    if book.isBorrow:
        book.isBorrow = False
        book.save()
        
        BorrowingHistory.objects.create(
            book=book,
            returned_date=timezone.now()
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
    


