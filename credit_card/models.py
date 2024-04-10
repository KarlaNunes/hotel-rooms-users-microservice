from django.db import models
from users.models import User

class CreditCard(models.Model):
    number = models.CharField(max_length=16, verbose_name="Card number")
    due_date = models.DateField(verbose_name="Card due date")
    owner = models.CharField(max_length=30, verbose_name="Credit card owner")
    cvv = models.CharField(max_length=3, verbose_name="CVV")
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"Credit card: {self.number}; "

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
