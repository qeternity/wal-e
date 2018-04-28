import json

from wal_e.blobstore import b2
from wal_e.storage.base import BackupInfo


class B2BackupInfo(BackupInfo):
    def load_detail(self, conn):
        if self._details_loaded:
            return

        uri = "{scheme}://{bucket}/{path}".format(
            scheme=self.layout.scheme,
            bucket=self.layout.store_name(),
            path=self.layout.basebackup_sentinel(self))

        data = json.loads(
            b2.uri_get_file(None, uri, conn=conn).decode())
        for k, v in list(data.items()):
            setattr(self, k, v)

        self._details_loaded = True
