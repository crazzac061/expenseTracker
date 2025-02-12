from django import forms
from .models import Category,Books

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']

class BookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=['title','category', 'author','publish_date']
        labels={'title':'Book Title','author':'Author Name'}