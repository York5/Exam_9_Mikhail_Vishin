from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotoIndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'photos'
    model = Photo
    ordering = ['-created_at']


class PhotoView(DetailView):
    template_name = 'photo.html'
    model = Photo


class PhotoCreateView(LoginRequiredMixin, CreateView):
    form_class = PhotoForm
    model = Photo
    template_name = 'create.html'

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = Photo.objects.create(author=self.request.user, photo=form.cleaned_data['photo'],
                                           description=form.cleaned_data['description'])
        return HttpResponseRedirect(self.get_success_url())


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    template_name = 'update.html'
    form_class = PhotoForm
    context_object_name = 'photo'
    permission_denied_message = 'Access Denied!'
    permission_required = 'webapp.change_photo'

    def has_permission(self):
        photo = Photo.objects.get(pk=self.kwargs['pk'])
        if photo.author == self.request.user or super().has_permission():
            return True

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = 'delete.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('webapp:index')
    permission_denied_message = 'Access Denied!'
    permission_required = 'webapp.delete_photo'

    def has_permission(self):
        photo = Photo.objects.get(pk=self.kwargs['pk'])
        if photo.author == self.request.user or super().has_permission():
            return True
