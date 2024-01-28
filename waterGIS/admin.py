from django.contrib import admin
from .models import User, UserProfile

# Register the User model
admin.site.register(User)

# Register the UserProfile model with custom admin settings


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_premium_user']
    list_filter = ['is_premium_user']
    search_fields = ['user__username', 'user__email']
