from django.contrib import admin
from .models import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AccountCreationForm

# class AccountAdmin(UserAdmin):
#     add_form = AccountCreationForm
#     form = AccountChangeForm
#     model = Account
#     list_display = ['full_name', 'email', 'phoneNumber', 'gender', 'is_superuser']

#admin.site.register(Account, AccountAdmin)

# Register your models here.
#admin.site.register(Account)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phoneNumber', 'gender', 'is_superuser')

# class AccountInstanceAdmin(admin.ModelAdmin):
#     list_filter = ('is_superuser', 'gender')


#admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Order_Product)
admin.site.register(ContactUs)
admin.site.register(Subscriber)
