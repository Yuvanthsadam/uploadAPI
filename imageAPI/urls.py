from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from uploadAPI.views import proListView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('uploadAPI.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
