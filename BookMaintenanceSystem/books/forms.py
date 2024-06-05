# from django import forms

from django import forms
from .models import BookCategory, BookCode, BookData, BookLendRecord
from accounts.models import Student

class BookForm(forms.Form):
    book_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    category_id = forms.ChoiceField(required=False, choices=[], widget=forms.Select(attrs={'class': 'form-select'}))
    borrower_id = forms.ChoiceField(required=False, choices=[], widget=forms.Select(attrs={'class': 'form-select'}))
    book_status = forms.ChoiceField(required=False, choices=[], widget=forms.Select(attrs={'class': 'form-select'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_id'].choices = [('', '----------------書籍類別----------------')] + list(BookCategory.objects.values_list('category_id', 'category_name'))
        self.fields['borrower_id'].choices = [('', '----------------借閱人------------------')] + list(Student.objects.values_list('id', 'username'))
        self.fields['book_status'].choices = [('', '----------------借閱狀態----------------')] + list(BookCode.objects.values_list('code_id', 'code_name'))


class BookCreateForm(forms.Form):
    book_name = forms.CharField(
        label="書名",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'bookname', 'required': True})
    )
    category_id = forms.ChoiceField(
        label="書籍類別",
        choices=[('', '----------------')] + [(category.category_id, category.category_name) for category in BookCategory.objects.all()],
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'inputState', 'required': True})
    )
    book_author = forms.CharField(
        label="作者",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'author'})
    )
    publisher = forms.CharField(
        label="出版社",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    publish_date = forms.DateField(
        label="出版日期",
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    summary = forms.CharField(
        label="內容簡介",
        max_length=1000,
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '最多輸入1000字', 'style': 'height: 200px'})
    )
    price = forms.DecimalField(
        label="價格",
        min_value=0,
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'price'})
    )
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price in [None, '']:
            return None
        return price
