from django.db import models


class Type_user(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class User(models.Model):
    id          = models.AutoField(primary_key=True)
    email_user  = models.EmailField()
    user_type   = models.ForeignKey(Type_user, on_delete=models.PROTECT, related_name='user_type')
    user_name   = models.CharField(max_length=200)
    first_name  = models.CharField(max_length=200,null=True, blank=True) # Allow empty & NULL
    last_name   = models.CharField(max_length=200,null=True, blank=True)
    birth_year  = models.DateField(null=True, blank=True)
    ddd_user    = models.IntegerField(null=True, blank=True)
    number_user = models.IntegerField(null=True, blank=True)
    photo       = models.ImageField(upload_to='login/', blank=True, null=True)
    
    def __str__(self):
        return self.user_name
