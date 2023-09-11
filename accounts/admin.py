from django.contrib import admin
from .models import UserBankAccount, UserAddress

# Register your models here.

class UserBankAccountAdmin(admin.ModelAdmin):
    list_display = ('account_no', 'user', 'account_type', 'birth_date', 'gender', 'initial_deposite_date', 'balance')

admin.site.register(UserBankAccount, UserBankAccountAdmin)

class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street_address', 'city', 'postal_code', 'country')
    
admin.site.register(UserAddress, UserAddressAdmin)
