from django.db import models

class User(models.Model):
    id          = models.AutoField(primary_key=True)
    email_user  = models.EmailField()
    user_name   = models.CharField(max_length=200)
    first_name  = models.CharField(max_length=200,null=True, blank=True) # Allow empty & NULL
    last_name   = models.CharField(max_length=200,null=True, blank=True)
    birth_year  = models.DateField(null=True, blank=True)
    ddd_user    = models.IntegerField(null=True, blank=True)
    number_user = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.user_name
