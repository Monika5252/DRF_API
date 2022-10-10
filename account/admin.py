from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *
class UserModelAdmin(BaseUserAdmin):
  list_display = ('id', 'email', 'name','mobile', 'is_admin','is_verify')
  list_filter = ('is_admin',)
  fieldsets = (
      ('User Credentials', {'fields': ('email', 'password')}),
      ('Personal info', {'fields': ('name', 'mobile')}),
      ('Permissions', {'fields': ('is_admin','is_verify',)}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'name', 'mobile', 'password1', 'password2'),

      }),
  )
  search_fields = ('email',)
  ordering = ('email', 'id')
  filter_horizontal = ()

admin.site.register(User, UserModelAdmin)

@admin.register(Demo)
class demoadmin(admin.ModelAdmin):
    list_display = ['id','name']

# # from django.contrib.auth import admin
# from django.contrib import admin
# admin.site.register(User)
