import unittest
from dropbox_webclient.helpers.dropbox_helper import DropboxClient, DropboxFile
from dropbox.exceptions import BadInputError, ApiError
from dropbox_webclient.tests.test_utils import TestUtils
from unittest.mock import MagicMock
from dropbox.files import WriteMode


class TestDropboxClient(unittest.TestCase, TestUtils):

    def setUp(self):
        self.dropbox_client = DropboxClient('<dropbox token>')
        self.dropbox_client.client = MagicMock(name='client')

    def test_check_connection_with_valid_token(self):
        self.dropbox_client._check_connection_()
        self.dropbox_client.client.users_get_current_account.assert_called_once_with()

    def test_check_connection_with_invalid_token(self):
        dropbox_client = DropboxClient('<not a valid token>')
        with self.assertRaises(BadInputError) as context:
            dropbox_client._check_connection_()
            self.assertTrue('Bearer <not a valid token>' in context.exception)

    def test_list_files(self):
        result = self.EmptyObject()
        result.entries = [self.DROPBOX_META_DATA_FILE1, self.DROPBOX_META_DATA_FILE2]
        self.dropbox_client.client.files_list_folder.return_value = result
        self.assertEqual(self.dropbox_client.list_files(), [self.DROPBOX_FILE1, self.DROPBOX_FILE2])

    def test_copy_file(self):
        self.dropbox_client.copy_file(self.LOCAL_FILE1)
        with open(self.LOCAL_FILE1, 'rb') as f:
            self.dropbox_client.client.client.files_upload(f.read(), '/' + self.LOCAL_FILE1_BASE_NAME,
                                                           mode=WriteMode('overwrite'))

    def test_delete_file(self):
        full_file_name = '/' + self.LOCAL_FILE1_BASE_NAME
        self.dropbox_client.delete_file(full_file_name)
        self.dropbox_client.client.files_delete.assert_called_once_with(full_file_name)
