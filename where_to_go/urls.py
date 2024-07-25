from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_map),
    path('places/<int:place_id>/', views.get_page_with_place, name='places'),
    path('tinymce/', include('tinymce.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
