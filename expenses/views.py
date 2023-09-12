from django.shortcuts import render, redirect
from .models import Expense
from django.http import JsonResponse


# List all expenses
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

# Add a new expense
def expense_add(request):
    # Handle the POST request
    if request.method == 'POST':
        # Validate and save the data here
        pass
    return render(request, 'expenses/expense_add.html')

# Edit an expense
def expense_edit(request, expense_id):
    # Fetch the expense by ID and ensure it belongs to the current user
    expense = Expense.objects.get(id=expense_id, user=request.user)
    # Handle the POST request
    if request.method == 'POST':
        # Validate and save the changes here
        pass
    return render(request, 'expenses/expense_edit.html', {'expense': expense})

# Delete an expense
def expense_delete(request, expense_id):
    # Fetch the expense by ID and ensure it belongs to the current user
    expense = Expense.objects.get(id=expense_id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return JsonResponse({'success': True})
