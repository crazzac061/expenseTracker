import pandas as pd
from .models import Category,Books
from django.shortcuts import get_object_or_404

def import_books(filename):
    df=pd.read_excel(filename)

    for _, row in df.iterrows():
        category,created=Category.objects.get_or_create(name=row['category'])
        book = Books.objects.filter(book_id=row['id']).first()

        if not book:
            # Create the book only if it doesn't already exist
            Books.objects.create(
                title=row['title'],
                subtitle=row['subtitle'],
                book_id=row['id'],
                authors=row['authors'],
                published_date=row['published_date'],
                distribution_expense=row['distribution_expense'],
                category=category
            )
        else:
            # Optionally, you can update the existing book's information
            print(f"Book with ID '{row['id']}' already exists.")
    
   

