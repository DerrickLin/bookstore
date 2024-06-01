# from django import forms

from django import forms
from .models import BookCategory, BookCode
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
