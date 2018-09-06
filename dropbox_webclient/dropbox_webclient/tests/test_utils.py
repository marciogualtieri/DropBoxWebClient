import dropbox_webclient
import os
from os.path import basename
from dropbox_webclient.helpers.dropbox_helper import DropboxFile
from dropbox.files import FileMetadata


class TestUtils:

    DROPBOX_META_DATA_FILE1 = FileMetadata(
        name='puppy1.jpg',
        size=208195,
        content_hash='015d99e0dbe76137f51084ece96a4619b2a4bad3dd642c908768fe7606a5fc86')

    DROPBOX_META_DATA_FILE2 = FileMetadata(
        name='puppy2.jpg',
        size=17258,
        content_hash='7134d42ebda1e833269c28fbe6980c55ea5d5dded8a9695d6e67b318b4bdf653')

    DROPBOX_FILE1 = DropboxFile.from_file_meta_data(DROPBOX_META_DATA_FILE1)

    DROPBOX_FILE2 = DropboxFile.from_file_meta_data(DROPBOX_META_DATA_FILE2)

    ROOT_PATH = os.path.dirname(dropbox_webclient.__file__)

    LOCAL_FILE1 = os.path.join(ROOT_PATH, 'resources/puppy2.jpg')

    LOCAL_FILE1_BASE_NAME = basename(LOCAL_FILE1)

    class EmptyObject:
        pass

