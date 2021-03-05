from django.db import models

from django.utils.timezone import now
from django.contrib.auth.models import User




class Expenses(models.Model):
    months = (
        ('January','January'),
        ('February','February'),
        ('March','March'),
        ('April','April'),
        ('May','May'),
        ('June','June'),
        ('July','July'),
        ('August','August'),
        ('September','September'),
        ('October','October'),
        ('November','November'),
        ('December','December'),
    )

    how = (
        ('Home','Home'),
        ('Construction','Construction'),
        ('Medical','Medical'),
        ('Education','Education'),
        ('Electronics','Electronics'),
        ('Services','Services'),
        ('Gifts','Gifts'),
        ('Travel','Travel'),
        ('Kids','Kids'),
        ('Furniture','Furniture'),
        ('Music','Music'),
        ('Pet','Pet'),
        ('Others','Others')
        
        
    )

    user = models.ForeignKey(User,related_name='creator', null=True,on_delete=models.CASCADE)    
    name = models.CharField(max_length=200,null=True,blank=True)
    amount = models.FloatField()
    reason = models.CharField(choices=how,max_length=1000,null=True,blank=True)
    important = models.BooleanField(default=False)   
    month = models.DateField(default=now)

    @property
    def totalexp(self):
        expenses = Expense.objects.all()
        total = sum([self.amount for expense in expenses])
        return total   


class Incomes(models.Model):
    months = (
        ('January','January'),
        ('February','February'),
        ('March','March'),
        ('April','April'),
        ('May','May'),
        ('June','June'),
        ('July','July'),
        ('August','August'),
        ('September','September'),
        ('October','October'),
        ('November','November'),
        ('December','December'),
    )

    how = (
        ('Home','Home'),
        ('Construction','Construction'),
        ('Medical','Medical'),
        ('Education','Education'),
        ('Electronics','Electronics'),
        ('Services','Services'),
        ('Gifts','Gifts'),
        ('Travel','Travel'),
        ('Kids','Kids'),
        ('Furniture','Furniture'),
        ('Music','Music'),
        ('Pet','Pet'),
        ('Others','Others')
        
        
    )

    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)    
    name = models.CharField(max_length=200,null=True,blank=True)
    amount = models.FloatField()
    reason = models.CharField(choices=how,max_length=1000,null=True,blank=True)
    important = models.BooleanField(default=False)   
    month = models.DateField(default=now)

    @property
    def totalexp(self):
        expenses = Expense.objects.all()
        total = sum([self.amount for expense in expenses])
        return total   
