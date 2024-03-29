from django.contrib import admin

from .models import User, Reply, Review, ReviewLike

admin.site.register(User)
# admin.site.register(Reply)
# admin.site.register(ReviewLike)


@admin.register(ReviewLike)
class ReviewLikeAdmin(admin.ModelAdmin):
    list_display = ["user", "review"]


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ["author", "parent_reply", "review"]
    list_filter = ["created_at", "author"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["name", "author", "created_at"]
    list_filter = ["created_at", "author"]
    search_fields = ["name", "comment"]
