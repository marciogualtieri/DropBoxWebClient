# -*- coding: utf-8 -*-

from django import forms


class UploadForm(forms.Form):

    upload_file = forms.FileField(label='Select a File to Upload')
