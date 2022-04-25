from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AccountsUser,Profile
from .forms import AccountUserChangeForm,AccountUserCreationForm

class AccountUserAdmin(UserAdmin):
    add_form = AccountUserCreationForm
    form = AccountUserChangeForm

    model = AccountsUser

    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser','last_login',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields' : ('username','email','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(AccountsUser, AccountUserAdmin)
admin.site.register(Profile)
