# -*- coding: utf-8 -*-
from django.conf.urls import url

import dropbox_webclient.uploader.views as uploader_views


urlpatterns = [
    url(r'^uploads/$', uploader_views.uploads, name='uploads')
]
