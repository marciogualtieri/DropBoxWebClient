# -*- coding: utf-8 -*-
import os
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from dropbox_webclient.uploader.models import Upload, DropboxInfo
from dropbox_webclient.uploader.forms import UploadForm

from dropbox_webclient.helpers.dropbox_helper import DropboxClient, DropboxFile

from django.conf import settings


@login_required(login_url='/accounts/login')
def uploads(request):
    dropbox_client = build_dropbox_client(request)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_file(request, dropbox_client)
            return HttpResponseRedirect('/uploader/uploads')
    else:
        form = UploadForm()
    uploads = dropbox_client.list_files()
    return render_to_response('uploads.html', {'uploads': uploads, 'form': form},
                              context_instance=RequestContext(request))


def build_dropbox_client(request):
    user = User.objects.get(username=request.user)
    try:
        dropbox_info = DropboxInfo.objects.get(user_id=user.id)
        return DropboxClient(dropbox_info.token)
    except DropboxInfo.DoesNotExist:
        raise Exception('You are required to have a valid Dropbox Token on your user profile.')


def upload_file(request, dropbox_client):
    new_upload = Upload(upload_file=request.FILES['upload_file'])
    new_upload.save()
    full_file_name = os.path.join(settings.MEDIA_ROOT, new_upload.upload_file.name)
    dropbox_client.copy_file(full_file_name)
