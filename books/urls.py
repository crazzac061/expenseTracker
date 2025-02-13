from django.urls import path
from .views import category_delete, category_create,category_list,category_update
urlpatterns=[path('categories/',category_list,name='category_list'),
             path('categories/new/',category_create,name='category_create'),
             path('categories/<int:pk>/edit',category_update,name='category_update'),
             path('categories/<int:pk>/delete/',category_delete,name='category_delete'),]
