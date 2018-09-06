from dropbox import Dropbox
from dropbox.files import WriteMode
from os.path import basename


class DropboxFile:

    def __init__(self, name, size, content_hash):
        self.name = name
        self.size = size
        self.content_hash = content_hash

    @classmethod
    def from_file_meta_data(cls, file_meta_data):
        return cls(file_meta_data.name, file_meta_data.size, file_meta_data.content_hash)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '<DropboxFile: name=%s, size=%d, content_hash=%s>' % (self.name, self.size, self.content_hash)

    def __eq__(self, the_other):
        return self.__dict__ == the_other.__dict__


class DropboxClient:

    def __init__(self, token):
        self.client = Dropbox(token)

    def list_files(self):
        self._check_connection_()
        return [DropboxFile.from_file_meta_data(file_meta_data)
                for file_meta_data in self.client.files_list_folder('').entries]

    def copy_file(self, full_file_name):
        self._check_connection_()
        with open(full_file_name, 'rb') as f:
            self.client.files_upload(f.read(), '/' + basename(full_file_name), mode=WriteMode('overwrite'))

    def delete_file(self, full_file_name):
        self._check_connection_()
        self.client.files_delete(full_file_name)

    def _check_connection_(self):
        self.client.users_get_current_account()
