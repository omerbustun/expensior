from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('add/', views.expense_add, name='expense_add'),
    path('edit/<int:expense_id>/', views.expense_edit, name='expense_edit'),
    path('delete/<int:expense_id>/', views.expense_delete, name='expense_delete'),
]
