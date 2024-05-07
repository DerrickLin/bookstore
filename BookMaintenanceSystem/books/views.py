from django.shortcuts import render

# Create your views here.
def Book(request):
    
    return render(request, 'book.html', locals())