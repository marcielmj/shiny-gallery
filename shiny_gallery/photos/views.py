from datetime import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from .forms import CommentForm
from .models import Photo


class PhotoListView(ListView):
    model = Photo
    queryset = Photo.objects.filter(is_approved=True)


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ("caption", "image")
    success_url = reverse_lazy("photos:photo-list")

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        return super().form_valid(form)


class PhotoDetailView(DetailView):
    model = Photo
    queryset = Photo.objects.filter(is_approved=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["liked"] = _check_user_likes(self.request.user, self.object)
        return context


class PhotoPendingApprovalView(PermissionRequiredMixin, PhotoListView):
    permission_required = ("photos.can_approve_photo",)
    queryset = Photo.objects.filter(is_approved=False)
    template_name_suffix = "_pending_approval"


@login_required
@require_http_methods(("POST",))
def like_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    liked = _check_user_likes(request.user, photo)

    if liked:
        photo.likes.remove(request.user)
    else:
        photo.likes.add(request.user)

    photo.save()
    return redirect("photos:photo-detail", pk=photo.pk)


@permission_required("photos.can_approve_photo")
@require_http_methods(("POST",))
def approve_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.approved_date = datetime.now()
    photo.is_approved = True
    photo.save()

    return redirect("photos:photo-detail", pk=photo.pk)


@login_required
@require_http_methods(("POST",))
def create_comment(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.photo = photo
        comment.user = request.user
        comment.save()

    return redirect("photos:photo-detail", pk=photo.pk)


def _check_user_likes(user, photo):
    return photo.likes.filter(id=user.id).count() > 0
