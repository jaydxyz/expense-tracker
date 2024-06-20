# views.py
from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

def home(request):
    expenses = Expense.objects.all()  # Retrieve all expenses from the database
    return render(request, 'home.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect 
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})