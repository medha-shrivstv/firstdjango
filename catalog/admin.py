from django.contrib import admin
from catalog.models import Book, Author, Genre,Borrow

# Register your models here.

# admin.site.register(Book)


 #admin.site.register(Genre)

 #admin.site.register(Author)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields=[('name', 'purchase_date')]
    search_fields = ('id','name')
    list_filter = ('name','purchase_date')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    pass


