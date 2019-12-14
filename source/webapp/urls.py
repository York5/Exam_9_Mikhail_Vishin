from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from webapp.views import PhotoIndexView, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'webapp'

urlpatterns = [
    path('', PhotoIndexView.as_view(), name='index'),
    path('photo/<int:pk>', PhotoView.as_view(), name='photo_view'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_add'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
