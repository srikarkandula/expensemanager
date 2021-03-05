from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Home,name='home'),
    path('expense/',Expense,name='Expense'),
    path('allexpense/',AllExpenditure,name='AllExpense'),
    path('expense/new',expenseNew,name='newexpense'),
    path('login/',loginPage,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('income/',Income,name='income'),
    path('incomeall/',AllIncome,name='AllIncome'),

    path('newincome/',incomeNew,name='newincome'),

    path('register/',Register,name='register'),

    path('expense/important',ImportantExpense,name='ImportantExpense'),
    #path('expense/chart',Chart,name='Chart'),
    

    path('expense/update/<int:pk>/',UpdateExpense,name='UpdateExpense'),
    path('expense/delete/<int:pk>/',DeleteExpense,name='DeleteExpense'),
    path('icnome/update/<int:pk>/',UpdateIncome,name='UpdateIncome'),
    path('icnome/delete/<int:pk>/',DeleteIncome,name='DeleteIncome'),
]