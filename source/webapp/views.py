from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Photo


class PhotoIndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'polls'
    model = Photo
    ordering = ['-created_at']


class PhotoView(DetailView):
    template_name = 'photo.html'
    model = Photo


class PollCreateView(CreateView):
    form_class = PhotoForm
    model = Photo
    template_name = 'create.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    model = Photo
    template_name = 'update.html'
    form_class = PhotoForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    model = Photo
    template_name = 'delete.html'
    context_object_name = 'poll'
    success_url = reverse_lazy('index')