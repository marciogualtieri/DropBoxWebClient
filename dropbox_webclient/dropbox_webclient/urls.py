from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin

import django.contrib.auth.views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^uploader/', include('dropbox_webclient.uploader.urls')),
    url(r'^$', RedirectView.as_view(url='/uploader/uploads/', permanent=True)),
    url(r'^accounts/login', auth_views.login),
    url(r'^accounts/logout', auth_views.logout),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
