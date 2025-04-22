from django.contrib import admin
from login.models import User

class Login_admin(admin.ModelAdmin):
    # it'll appear on website admin of django 
    list_display = (
        'id', 'email_user', 'user_name', 'first_name', 
        'last_name', 'birth_year', 'ddd_user', 'number_user')
    search_fields = ('user_name',)

# Must be registered the User and the Login_admin to appear
admin.site.register(User, Login_admin)
