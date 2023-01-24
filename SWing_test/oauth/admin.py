from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .forms import UserCreationForm, UserChangeForm
from .models import User
# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    
    list_display = ('student_id', 'email', 'username', 'is_active', 'is_superuser', 'is_admin', 'is_staff')
    list_filter = ('is_active', 'is_superuser', 'is_admin', 'is_staff')
    
    filedsets = (
        (None, {'fileds': ('student_id', 'email', 'username')}),
        (_('Permissions'), {'fileds': ('is_active', 'is_superuser', 'is_admin', 'is_staff')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('student_id', 'email', 'username')}
         ),
    )
    search_fields = ('student_id', 'email', 'username')
    ordering = ('student_id', )
    filter_horizontal = ()
    
admin.site.register(User, UserAdmin)