from django.db import models
from users.models import User

class CreditCard(models.Model):
    number = models.CharField(max_length=16, verbose_name="Card number")
    due_date = models.DateField(verbose_name="Card due date")
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    cvv = models.CharField(max_length=3, verbose_name="CVV")    
    
    def __str__(self):
        return f"Credit card: {self.number}; "

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
