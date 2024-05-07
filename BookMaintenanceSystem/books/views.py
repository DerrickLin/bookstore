from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db.models import Q, Case, When, Value, CharField, F
from .models import BookData, BookCategory, BookCode, BookLendRecord
from accounts.models import Student
# from .forms import BookQueryForm

# Create your views here.
def Book(request):
    categories = list(BookCategory.objects.values_list('category_id', 'category_name'))
    usernames = list(Student.objects.values_list('id', 'username'))
    bookstatus = list(BookCode.objects.values_list('code_id', 'code_name'))
    books = BookData.objects.all()

    
    if request.method == "POST":
    
        book_name = request.POST.get("book_name")
        category_id = request.POST.get("category_id")
        borrower_id = request.POST.get("borrower_id")
        book_status = request.POST.get("book_status")
            
        conditions = Q()
        if book_name:
            conditions &= Q(name__contains=book_name)
        if category_id:
            conditions &= Q(category_id=category_id)
        if borrower_id:
            conditions &= Q(keeper_id=borrower_id)
        if book_status:
            conditions &= Q(status_id=book_status)
        books = books.filter(conditions)

        
    return render(request, 'book.html', locals())