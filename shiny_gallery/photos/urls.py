from django.urls import path

from .views import (
    PhotoDetailView,
    PhotoListView,
    PhotoCreateView,
    PhotoPendingApprovalView,
    like_photo,
    approve_photo,
    create_comment,
)

app_name = "photos"

urlpatterns = [
    path("", PhotoListView.as_view(), name="photo-list"),
    path("add/", PhotoCreateView.as_view(), name="photo-add"),
    path("<uuid:pk>/", PhotoDetailView.as_view(), name="photo-detail"),
    path("<uuid:pk>/like/", like_photo, name="photo-like"),
    path("<uuid:pk>/comments/", create_comment, name="comment-add"),
    path("<uuid:pk>/approve", approve_photo, name="photo-approve"),
    path("pending_approval/", PhotoPendingApprovalView.as_view(), name="photo-pending-approval"),
]
