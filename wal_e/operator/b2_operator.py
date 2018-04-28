from wal_e.blobstore.b2 import calling_format
from wal_e.operator.backup import Backup
from wal_e.worker.b2 import b2_worker


class B2Backup(Backup):
    def __init__(self, layout, creds, gpg_key_id):
        super(B2Backup, self).__init__(layout, creds, gpg_key_id)
        self.cinfo = calling_format
        self.worker = b2_worker
