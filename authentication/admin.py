from django.contrib import admin
from authentication.models import User, UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_superuser",)
    list_editable = ("email","is_staff", )
    list_display_links = ("username",)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "nationality",)
    list_editable = ("first_name", "last_name", "nationality",)
    list_display_links = ("user",)

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)