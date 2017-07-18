from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from web import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^about', views.about),
    url(r'^portfolio', views.portfolio),
    url(r'^contact', views.contact)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
