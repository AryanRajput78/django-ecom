from django.contrib import admin
from . models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.



# for hiding password field from admin, list whatever you want to show on admin page, only that'll show
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    #it'll show links only these fields in admin panel
    list_display_links = ('email', 'first_name','last_name')
    # you can only read these fields
    readonly_fields = ('last_login','date_joined')
    # date joined sorting
    ordering = ('-date_joined',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Account, AccountAdmin)