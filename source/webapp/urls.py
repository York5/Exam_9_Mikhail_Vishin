from django.urls import path
from webapp.views import IndexView
from django.conf.urls.static import static
from django.conf import settings


app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
