from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from dropbox_webclient.uploader.models import Upload
from dropbox_webclient.uploader.models import DropboxInfo


class DropboxInfoInline(admin.StackedInline):
    model = DropboxInfo
    can_delete = False
    verbose_name_plural = 'dropbox_info'


class UserAdmin(BaseUserAdmin):
    inlines = (DropboxInfoInline,)


# Register your models here.
admin.site.register(Upload)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
