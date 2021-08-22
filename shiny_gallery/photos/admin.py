from django.contrib import admin

from .models import Comment, Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "caption", "uploader", "timestamp", "is_approved")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "user", "timestamp")
