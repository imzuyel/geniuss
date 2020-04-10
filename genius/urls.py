
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('', include('courses.urls')),
    path('tinymce/', include('tinymce.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
