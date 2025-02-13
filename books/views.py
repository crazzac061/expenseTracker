from django.shortcuts import render,redirect,get_object_or_404
from .models import Books,Category
from .forms import BookForm,CategoryForm

# Create your views here.
def category_list(request):
     category=Category.object.all()
     return redirect(request, 'book/category_list.html',{'category':category})
def category_create(request):
     if request.method=='POST':
          form=CategoryForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('category_list')
     else:
          form=CategoryForm()
     return render(request,'books/category_form.html',{'form':form})
def category_update(request,pk):
     category=get_object_or_404(Category,pk=pk)
     if request.method=='Post':
          form=CategoryForm(request.POST,instance=category)
          if form.is_valid():
               form.save()
               return redirect('category_list')
     else:
          form=CategoryForm(instance=category)
     return render(request, 'bppks/category_form.html',{'form':form})
def category_delete(request,pk):
     category=get_object_or_404(Category,pk=pk)
     if request.method=='POST':
          category.delete()
          return redirect('category_list')
     return render(request,'books/category_confirm_delete.html',{'category':category})


