import datetime
import requests

from dataclasses import dataclass
from typing import Optional
from TemporaryStorage.providers import Provider, File, HostedFile


@dataclass
class ProviderInstance(Provider):
    def __provider_init__(self):
        self.provider = 'qu.ax'
        self.max_file_size = 100
        self.min_retention = None
        self.max_retention = None
        self.base_url = 'https://qu.ax'

    def __calc_retention_date__(self) -> Optional[datetime.datetime]:
        return self.max_retention

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
