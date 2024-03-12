from django.contrib import admin
from books.models import Book, BookAuthor, BookReview, Author


# Register your models here.

# admin.site.register(Author)
# admin.site.register(BookAuthor)
# admin.site.register(BookReview)

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn')
    list_display = ('title', 'isbn', 'description',)
    fields = (('title', 'isbn'), 'description', "cover_picture")


class AuthorAdmin(admin.ModelAdmin):
    pass


class BookAuthorAdmin(admin.ModelAdmin):
    pass


class BookReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookReview, BookReviewAdmin)
