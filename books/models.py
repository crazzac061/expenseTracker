from django.db import models



class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
class Books(models.Model):
    title=models.CharField(max_length=255,unique=True)
    subtitle=models.CharField(max_length=255)
    book_id=models.BigIntegerField(primary_key=True)
    authors=models.CharField(max_length=255)
    published_date=models.DateField()
    distribution_expense=models.DecimalField(max_digits=10, decimal_places=4)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
