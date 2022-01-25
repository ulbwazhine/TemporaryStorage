import datetime
import requests

from dataclasses import dataclass
from typing import Optional
from TemporaryStorage.providers import Provider, File, HostedFile


@dataclass
class ProviderInstance(Provider):
    def __provider_init__(self):
        self.provider = 'transfer.sh'
        self.max_file_size = None
        self.min_retention = 14
        self.max_retention = 14
        self.base_url = 'https://transfer.sh'

    def __calc_retention_date__(self) -> datetime:
        return datetime.datetime.utcnow() + datetime.timedelta(days=self.max_retention)

    def check_file(self, file: File) -> bool:
        if file.file_size > self.max_file_size:
            return False

        return True

    def upload(self, file: File) -> Optional[HostedFile]:
        req = requests.post(self.base_url,
                            files={"file": open(file.path, 'rb')})

        if req.status_code != 200:
            return

        return HostedFile(
            provider=self.provider,
            url=req.text.split('\n')[0].replace('https://transfer.sh/', 'https://transfer.sh/get/'),
            retention_to=self.__calc_retention_date__()
        )
