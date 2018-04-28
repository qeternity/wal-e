try:
    import b2client
    assert b2client
except ImportError:
    from wal_e.exception import UserException
    raise UserException(
        msg='Backblaze support requires the module "python-b2" ',
        hint='Try running "pip install python-b2')

from wal_e.blobstore.b2.credentials import Credentials
from wal_e.blobstore.b2.utils import (
    do_lzop_get, uri_put_file, uri_get_file, write_and_return_error)

__all__ = [
    'Credentials',
    'do_lzop_get',
    'uri_put_file',
    'uri_get_file',
    'write_and_return_error'
]
