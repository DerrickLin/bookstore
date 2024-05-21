from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db.models import Q
from .models import BookData, BookCategory, BookCode, BookLendRecord
from accounts.models import Student
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

# Create your views here.
@csrf_exempt
@login_required(login_url='/login/')
def Book(request):
    categories = list(BookCategory.objects.values_list('category_id', 'category_name'))
    usernames = list(Student.objects.values_list('id', 'username'))
    bookstatus = list(BookCode.objects.values_list('code_id', 'code_name'))
    books = BookData.objects.all()
    students = Student.objects.all().values('id', 'username')
    # 取得錯誤訊息
    message = request.GET.get('message', '')
    
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


@login_required(login_url='/login/')
def book_detail(request, book_id):
    book = get_object_or_404(BookData, id=book_id)
    # 取得錯誤訊息
    message = request.GET.get('message', '')
    message_ok = request.GET.get('message_ok', '')
    keeper_name = None
    if book.keeper_id:
        keeper = get_object_or_404(Student, id=book.keeper_id)
        keeper_name = keeper.username
    return render(request, 'book_detail.html', locals())


@login_required(login_url='/login/')
def book_create(request):
    categories = list(BookCategory.objects.values_list('category_id', 'category_name'))
    usernames = list(Student.objects.values_list('id', 'username'))
    bookstatus = list(BookCode.objects.values_list('code_id', 'code_name'))
    message = request.GET.get('message', '')
    
    if request.method == "POST":
        book_name = request.POST.get("book_name")
        category_id = request.POST.get("category_id")
        author = request.POST.get("book_author")
        publisher = request.POST.get("publisher")
        publish_date = request.POST.get("publish_date")
        summary = request.POST.get("summary")
        price = request.POST.get("price")
        borrower_id = request.POST.get("borrower_id")
        book_status = request.POST.get("book_status")
    
        # 檢查價格是否是空字符串
        if price == '':
            price = None
        else:
            price = int(price)
            
        # 檢查出版日期是否是空字符串
        if publish_date == '':
            publish_date = None
        
        # 檢查借閱者是否是為空
        if borrower_id == '':
            # 如果借閱者是空，則不允許新增，並且顯示錯誤訊息
            message = '未選擇借閱者，無法新增'
            redirect_url = reverse('Create') + '?message=' + message
            return HttpResponseRedirect(redirect_url)
        
        category = BookCategory.objects.get(category_id=category_id)
        status = BookCode.objects.get(code_id=book_status)
        # 新增書籍資料
        book = BookData(name=book_name, category=category, author=author, publisher=publisher, publish_date=publish_date, summary=summary, price=price, keeper_id=borrower_id, status=status)
        book.save()
        
        # 如果有借閱者，新增借閱紀錄
        if borrower_id:
            borrowers = Student.objects.get(id=borrower_id)
            lend_record = BookLendRecord(book=book, borrower=borrowers, borrow_date=datetime.now().date())
            lend_record.save()
            
        # 新增成功後，導向書籍清單頁面
        message = '成功新增 ⟪ ' + book_name + ' ⟫ 書籍'
        redirect_url = reverse('Book') + '?message=' + message
        return HttpResponseRedirect(redirect_url)
    
    return render(request, 'book_create.html', locals())


@login_required(login_url='/login/')
def book_lend_records(request, book_id):
    book = get_object_or_404(BookData, id=book_id)
    # 取得書籍的借閱紀錄 (依借閱日期排序)
    lend_records = BookLendRecord.objects.filter(book=book).order_by('-borrow_date')
    return render(request, 'book_lend_records.html', locals())


@login_required(login_url='/login/')
def book_edit(request, book_id):
    book = get_object_or_404(BookData, id=book_id)
    categories = list(BookCategory.objects.values_list('category_id', 'category_name'))
    usernames = list(Student.objects.values_list('id', 'username'))
    bookstatus = list(BookCode.objects.values_list('code_id', 'code_name'))
    
    if book.keeper_id:
        keeper = get_object_or_404(Student, id=book.keeper_id)
        keeper_name = keeper.username
        
    if request.method == "POST":
        book_name = request.POST.get("book_name")
        category_id = request.POST.get("category_id")
        author = request.POST.get("book_author")
        publisher = request.POST.get("publisher")
        publish_date = request.POST.get("publish_date")
        summary = request.POST.get("summary")
        price = request.POST.get("price")
        borrower_id = request.POST.get("borrower_id")
        book_status = request.POST.get("book_status")
        
        # 檢查價格是否是空字符串
        if price == '':
            price = None
        else:
            price = int(price)

        # 檢查出版日期是否是空字符串
        if publish_date == '':
            publish_date = None
        
        if borrower_id == '':
            # 如果借閱者是空，則不允許編輯，並且顯示錯誤訊息
            message = '未選擇借閱者，無法編輯'
            redirect_url = reverse('Detail', args=[book.id]) + '?message=' + message
            return HttpResponseRedirect(redirect_url)
            
        category = BookCategory.objects.get(category_id=category_id)
        status = BookCode.objects.get(code_id=book_status)
        
        # 更新書籍資料
        BookData.objects.filter(id=book_id).update(name=book_name, category=category, author=author, publisher=publisher, publish_date=publish_date, summary=summary, price=price, keeper_id=borrower_id, status=status)
        
        # 如果有借閱者，新增借閱紀錄
        if borrower_id:
            borrowers = Student.objects.get(id=borrower_id)
            lend_record = BookLendRecord(book=book, borrower=borrowers, borrow_date=datetime.now().date())
            lend_record.save()
            
        # 編輯成功後，導向書籍詳細頁面    
        message_ok = f'⟪ {book_name} ⟫ 書籍編輯成功'
        redirect_url = reverse('Detail', args=[book.id]) + '?message_ok=' + message_ok
        return HttpResponseRedirect(redirect_url)
    return render(request, 'book_edit.html', locals())


@csrf_exempt
@login_required(login_url='/login/')
def book_delete(request, book_id):
    book = get_object_or_404(BookData, id=book_id)
    # 如果書籍狀態是借出中，則無法刪除
    if book.status.code_id == 'B':
        return JsonResponse({'message': 'unable'})
    else:
        book.delete()
        return JsonResponse({'message': 'success'})
       
    
    
