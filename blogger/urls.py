
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from blogger.blog.views import blog
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('tinymce/', include('tinymce.urls')),
]  
# add this lines
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = "blog.views.error_404"
handler505 = "blog.views.error_505"
