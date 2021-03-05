from django.shortcuts import render,redirect
from .models import *
from django.views.generic import CreateView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import *

from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required

from .filters import ExpensesFilter

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages



@login_required(login_url='login')
def Home(request):
    expense = Expenses.objects.all().order_by('-id')
    expenses = expense.filter(user=request.user)
    expense_count = Expenses.objects.all().count()

    income = Incomes.objects.all()
    incomes = income.filter(user=request.user)
    income_count = Incomes.objects.all().count()

    a = 0
    for expense in expenses:
        a = a+expense.amount

    b=0

    for income in incomes:
        b = b+income.amount

    c = b-a

    context = {
        'expenses':expenses,'expense_count':expense_count,'income_count':income_count,'a':a,'b':b,'d':c,
    }

    return render(request,'main.html',context)

@login_required(login_url='login')
def Expense(request):

    expenses = []

    expense = Expenses.objects.all().order_by('-id')
    expenses = expense.filter(user=request.user)
    


    #expenses_list = request.user.expenses.all()('-id')
    #expense_count = expenses.count()
    paginator = Paginator(expenses,5)
    page = request.GET.get('page')
    
    expense_count = expenses.count()

    a = 0

    for xpense in expenses:
        a+=xpense.amount


    try:
        post5 = paginator.page(page)
    except PageNotAnInteger:
        post5 = paginator.page(1)
    except EmptyPage:
        post5 = paginator.page(paginator.num_pages)        

    a = 0




   




    context = {
        'a':a,'expense_count':expense_count,'expenses':post5
        
        #'a':a,'expenses':post5,'expense_count':expense_count,
        #'January':January,'February':February,'March':March,'April':April,
        #'May':May,'June':June,'July':July,'August':August,'September':September,
        #'October':October,'November':November,'December':December
    }
    return render(request,'Expenditure.html',context)

@login_required(login_url='login')
def expenseNew(request):

    form = NewExpenseForm()

   
    if request.method=="POST":
        form = NewExpenseForm(request.POST)
        if form.is_valid:
            Expense.user = request.user
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('/expense')



    context = {'form':form}
     

    return render(request,'newexpense.html',context)



@login_required(login_url='login')
def UpdateExpense(request,pk):
    expense = Expenses.objects.get(id=pk)
    form = NewExpenseForm(instance=expense)
    if request.method=="POST":
        form = NewExpenseForm(request.POST, instance=expense)
        if form.is_valid:
            form.save()
            return redirect('/expense')
    context = {'form':form}    
    return render(request,'updateexpense.html',context)

@login_required(login_url='login')
def DeleteExpense(request,pk):
    expense = Expenses.objects.get(id=pk)
    if request.method=="POST":
        expense.delete()
        return redirect('/expense')
    context = {'expense':expense}

    return render(request,'deleteexpense.html',context)

@login_required(login_url='login')
def AllExpenditure(request):
    expense = Expenses.objects.all().order_by('-id')
    expenses = expense.filter(user=request.user)
    expensess = Expenses.objects.all()
    expense_important = expenses.filter(important="True")

    

    context = {'expenses':expenses,'expense_important':expense_important}
    return render(request,'allexpenditure.html',context)

@login_required(login_url='login')
def ImportantExpense(request):
    expense = Expenses.objects.all().order_by('-id')
    expenses = expense.filter(user=request.user)
    expense_important = expenses.filter(important="True")
    context = {'expenses':expenses,'expense_important':expense_important}

    return render(request,'importantexpense.html',context)





@login_required(login_url='login')
def Income(request):

    expenses = []

    expense = Incomes.objects.all().order_by('-id')
    expenses = expense.filter(user=request.user)
    
    #expenses_list = request.user.expenses.all()('-id')
    #expense_count = expenses.count()
    paginator = Paginator(expenses,5)
    page = request.GET.get('page')
    
    expense_count = expenses.count()

    a = 0

    for xpense in expenses:
        a+=xpense.amount


    try:
        post5 = paginator.page(page)
    except PageNotAnInteger:
        post5 = paginator.page(1)
    except EmptyPage:
        post5 = paginator.page(paginator.num_pages)        

    a = 0




   




    context = {
        'a':a,'expense_count':expense_count,'expenses':post5
        
        #'a':a,'expenses':post5,'expense_count':expense_count,
        #'January':January,'February':February,'March':March,'April':April,
        #'May':May,'June':June,'July':July,'August':August,'September':September,
        #'October':October,'November':November,'December':December
    }
    return render(request,'incomes.html',context)

@login_required(login_url='login')
def incomeNew(request):

    form = NewIncomeForm()

   
    if request.method=="POST":
        form = NewIncomeForm(request.POST)
        if form.is_valid:
            Income.user = request.user
            income = form.save(commit=True)
            income.user = request.user
            income.save()
            return redirect('/income')



    context = {'form':form}
     

    return render(request,'newincome.html',context)



@login_required(login_url='login')
def UpdateIncome(request,pk):
    income = Incomes.objects.get(id=pk)
    form = NewIncomeForm(instance=income)
    if request.method=="POST":
        form = NewIncomeForm(request.POST, instance=income)
        if form.is_valid:
            form.save()
            return redirect('/income')
    context = {'form':form}    
    return render(request,'updateincome.html',context)

@login_required(login_url='login')
def DeleteIncome(request,pk):
    income = Incomes.objects.get(id=pk)
    if request.method=="POST":
        income.delete()
        return redirect('/income')
    context = {'expense':income}

    return render(request,'deleteincome.html',context)

@login_required(login_url='login')
def AllIncome(request):
    expense = Incomes.objects.all().order_by('-id')
    expenses = expense.filter(user=request.user)
    expensess = Incomes.objects.all()
    expense_important = expenses.filter(important="True")

    

    context = {'expenses':expenses,'expense_important':expense_important}
    return render(request,'allincome.html',context)







def Register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
             
            messages.success(request,'Account was created succesfully for '+user)
            
    
            return redirect('login')


    context = {'form':form}

    return render(request,'register.html',context)


def loginPage(request):

    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)   
            return redirect('home') 
            
        else:
            messages.info(request,'Username or Password is incorrect')
            
    context={}

    return render(request,'login.html',context)


def logoutUser(request):
    logout(request)


    return redirect('login')





