from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Profile, AuditEntry, Parent, Teacher

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email', 'last_name', 'first_name', 'middle_name', 'date_joined', 'last_login']
    list_filter = ('is_teacher', 'is_parent', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (('User'), {'fields': ('username', 'email', 'phone_number', 'password','first_name', 'last_name', 'middle_name',
         'birth_date','is_staff', 'is_superuser', 'is_active', 'is_parent', 'is_teacher')}),
    )#add fields here after adding from models.py
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','password1', 'password2', 'email', 'phone_number', 'first_name', 'last_name', 'middle_name',
         'birth_date','is_staff', 'is_superuser', 'is_active', 'is_parent', 'is_teacher' ),
        }),
    )

@admin.register(AuditEntry)
class AuditEntryAdmin(admin.ModelAdmin):
    list_display = ['action', 'username', 'ip', 'time']
    list_filter = ['action',]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Parent)
admin.site.register(Teacher)
# Register your models here.
