from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from posts.views import index, about, contact, browse, search, PostDetailView

urlpatterns = [
    path('', index, name='home'),
    path('post/<int:pk>/detail/', PostDetailView.as_view(), name='post-detail'),
    path('search/', search, name='search'),
    path('browse/', browse, name='browse'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)