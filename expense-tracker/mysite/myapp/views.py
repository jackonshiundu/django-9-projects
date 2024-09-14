from django.shortcuts import render,redirect
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
from datetime import datetime, timedelta

# Create your views here.
def index(request):

    if request.method=="POST":
        form_data=ExpenseForm(request.POST)
        if form_data.is_valid():
            form_data.save()
    
    expenses=Expense.objects.all()
    total_expenses=expenses.aggregate(Sum('amount'))
    ##logic to calculculate 365 days

    last_year = datetime.now() - timedelta(days=1)
    data=Expense.objects.filter(date__gt=last_year)
    yearly_sum=data.aggregate(Sum('amount'))
    ##logic to calculculate last 30 days

    last_month = datetime.now() - timedelta(days=30)
    data=Expense.objects.filter(date__gt=last_month)
    monthly_sum=data.aggregate(Sum('amount'))

    ##logic to calculculate last week

    last_week = datetime.now() - timedelta(days=7)
    data=Expense.objects.filter(date__gt=last_week)
    weekly_sum=data.aggregate(Sum('amount'))

    daily_sums=Expense.objects.filter().values('date').annotate(sum=Sum('amount'))
    category_sums=Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))
    print(category_sums)

    expense_form=ExpenseForm()
    
    return render(request,'myapp/index.html',{'expense_form':expense_form,'expenses':expenses,'total_expenses':total_expenses,'yearly_sum':yearly_sum,'monthly_sum':monthly_sum,'weekly_sum':weekly_sum,'daily_sums':daily_sums,'category_sums':category_sums})

def edit(request,id):
    expense=Expense.objects.get(id=id)
    expense_form=ExpenseForm(instance=expense)

    if request.method =="POST":
        expense=Expense.objects.get(id=id)
        form =ExpenseForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'myapp/edit.html',{'expense_form':expense_form})


def delete(request,id):
    if request.method=="POST" and 'delete' in request.POST:  
        expense=Expense.objects.get(id=id)
        expense.delete()
    return redirect('index')