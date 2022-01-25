import datetime
import requests

from dataclasses import dataclass
from typing import Optional
from TemporaryStorage.providers import Provider, File, HostedFile


@dataclass
class ProviderInstance(Provider):
    def __provider_init__(self):
        self.provider = 'cockfile~'
        self.max_file_size = 2048
        self.min_retention = 2
        self.max_retention = 2
        self.base_url = 'https://cockfile.com'

    def __calc_retention_date__(self) -> datetime:
        return datetime.datetime.utcnow() + datetime.timedelta(days=self.max_retention)

    def check_file(self, file: File) -> bool:
        if file.file_size > self.max_file_size:
            return False

        return True

    def upload(self, file: File) -> Optional[HostedFile]:
        req = requests.post(self.base_url + '/upload.php', files={"files[]": open(file.path, 'rb')})

        if req.status_code != 200:
            return

        if not req.json().get('success'):
            return

        return HostedFile(
            provider=self.provider,
            url=req.json().get('files', [])[-1].get('url'),
            retention_to=self.__calc_retention_date__()
        )

