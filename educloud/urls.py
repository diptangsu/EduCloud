from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings
import users.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users.views.login, name='login'),
    path('user/', include('users.urls')),
    path('academics/', include('academics.urls')),
    path('question/', include('questions.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
