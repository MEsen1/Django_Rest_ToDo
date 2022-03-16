from django.db import models

# Create your models here.


class Todo(models.Model):
    task = models.CharField(max_length=50)
    description = models.TextField()
    
    TITLE = {
        ('H','High'),
        ('M','Medium'),
        ('L','Low')
        
    }
    
    priority = models.CharField(max_length=50,choices= TITLE)
    done= models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.task}'
    