#models.py
from django.db import models

class Expense(models.Model):
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=50, default='Uncategorized')  # Add default value