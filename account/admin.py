from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User

@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display = ["id", "username", "first_name", "last_name", "email"]
    filter_horizontal = ["groups", "user_permissions"]
    list_filter = ["role"]
    fieldsets = (
        ("User Credentails", {"fields" : ("username", "password")}),
        ("Personal Information", {"fields" : ("first_name", "last_name", "email", "role")}),
        ("Permissions", {"fields" : ("is_active", "is_staff" ,"is_superuser")}),
        ("Groups and Permissions", {"fields" : ("groups", "user_permissions")}),
        ("Important Dates", {"fields" : ("created_at", "updated_at", "last_login")})
    )
    readonly_fields = ["created_at", "updated_at"]
    sorted = ["id"]
    search_fields = ["username"]