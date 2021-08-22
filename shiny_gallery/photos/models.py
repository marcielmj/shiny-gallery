from datetime import datetime
import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    caption = models.CharField(max_length=255, blank=True, default="")
    image = models.ImageField(upload_to="uploads/%Y")
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="likes")
    timestamp = models.DateTimeField(default=datetime.now)
    approved_date = models.DateTimeField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name="uploads")

    @property
    def likes_count(self):
        return self.likes.count()

    @property
    def comments_count(self):
        return self.comments.count()

    def __str__(self):
        return f"Photo {self.pk} by {self.uploader}"

    def get_absolute_url(self):
        return reverse("photo-detail", {"pk": self.pk})

    class Meta:
        ordering = ("-approved_date", "-timestamp")
        permissions = (("can_approve_photo", "Can approve photo"),)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments+")
    photo = models.ForeignKey("photos.Photo", on_delete=models.CASCADE, related_name="comments")
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Comment {self.pk}"

    class Meta:
        ordering = ("timestamp",)
