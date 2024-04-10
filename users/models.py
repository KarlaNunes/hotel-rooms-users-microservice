from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30, verbose_name="User name")
    social_security_card = models.CharField(max_length=11, verbose_name="Social security card")
    contact = models.CharField(max_length=15)
    
    
    def __str__(self):
        return f"User: {self.name}; Social security card: {self.social_security_card}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"