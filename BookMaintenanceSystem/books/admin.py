from django.contrib import admin
from . import models
# Register your models here.

class BookDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'author')

admin.site.register(models.BookData, BookDataAdmin)


class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')
    search_fields = ('category_name',)
admin.site.register(models.BookCategory, BookCategoryAdmin)


class BookLendRecordAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrow', 'borrow_date')
    search_fields = ('book', 'borrow')
admin.site.register(models.BookLendRecord, BookLendRecordAdmin)


class BookCodeAdmin(admin.ModelAdmin):
    list_display = ('code_id', 'code_name')
    search_fields = ('code_name',)
admin.site.register(models.BookCode, BookCodeAdmin)