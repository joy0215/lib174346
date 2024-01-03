from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    write = models.CharField(max_length=50, default="不詳")
    slug = models.CharField(max_length=200)
    bookstype=[("一般書籍","一般書籍"),("教學用書","教學用書")]
    category = models.CharField(max_length=20, choices=bookstype, default="一般書籍")
    intro = models.TextField(default="", blank=True)
    photolink = models.TextField(default="", blank=True)
    body = models.TextField()
    isBorrow = models.BooleanField(_("外借中"), default=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    @property
    def formatted_is_borrow(self):
        if self.isBorrow:
            return '<span style="color: white; background-color: red; border: 1px solid white; padding: 3px; border-radius: 3px;">外借中</span>'
        else:
            return '<span style="color: white; background-color: green; border: 1px solid white;padding: 3px; border-radius: 3px;">可借閱</span>'

    formatted_is_borrow.fget.short_description = "外借狀態"
    
    class Meta:
        ordering = ("-pub_date",) 
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text


class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1),
        ),
    ]
    
from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    is_borrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class BorrowingHistory(models.Model):
    book = models.ForeignKey(Post, on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=100)
    borrowed_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} - {self.borrower_name}"

class BorrowingHistor2(models.Model):
    book = models.ForeignKey(Post, on_delete=models.CASCADE)
    br = models.CharField(max_length=50)
    date = models.DateField()


    def __str__(self):
        return f"{self.book.title}"
    