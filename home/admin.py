'''from django.contrib import admin
from home.models import Book, Author, Genre

# Register your models here.

# admin.site.register(Book)


 #admin.site.register(Genre)

 #admin.site.register(Author)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
    # search_fields = ('id','name')
    # list_filters = ('name','purchase_date')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass'''

