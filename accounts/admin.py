from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser as Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'full_name', 'phone_number', 'date_joined', 'last_login', 'is_staff')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)