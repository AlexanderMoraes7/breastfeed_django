from django.contrib import admin
from login.models import Type_user


class Type_admin(admin.ModelAdmin):
    # it'll appear on website admin of django 
    # Aparecerá no site do django admin
    list_display = ('name',)
    search_fields = ('name',)


# Must be registered the Type_user and the Type_admin to appear
# Deve ser registrado o type_user e o type_admin para aparecer
admin.site.register(Type_user, Type_admin)
