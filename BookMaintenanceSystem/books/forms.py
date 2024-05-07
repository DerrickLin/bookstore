# from django import forms

# class BookQueryForm(forms.Form):
#     book_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     category_id = forms.ChoiceField(required=False, choices=[])
#     borrower_id = forms.ChoiceField(required=False, choices=[])
#     book_status = forms.ChoiceField(required=False, choices=[])
    
#     def __init__(self, *args, **kwargs):
#         categories = kwargs.pop('categories', [])
#         usernames = kwargs.pop('usernames', [])
#         bookstatus = kwargs.pop('bookstatus', [])
#         super(BookQueryForm, self).__init__(*args, **kwargs)

#         self.fields['category_id'].choices = [('', '----------------書籍類別----------------')] + [(category_id, category_name) for category_id, category_name in categories]
#         self.fields['borrower_id'].choices = [('', '----------------借閱人---------------')] + usernames
#         self.fields['book_status'].choices = [('', '----------------借閱狀態----------------')] + bookstatus