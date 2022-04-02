from django.conf.urls.static import static
from django.urls import path
from .views import index
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)