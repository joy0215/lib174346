from django.contrib import admin
from mysite.models import Post,Product



# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=("title","write","formatted_is_borrow","category","intro","slug","pub_date","id")


admin.site.register(Post,PostAdmin)
admin.site.register(Product)