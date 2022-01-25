import datetime
import requests

from dataclasses import dataclass
from typing import Optional
from TemporaryStorage.providers import Provider, File, HostedFile


@dataclass
class ProviderInstance(Provider):
    def __provider_init__(self):
        self.provider = 'x0.at'
        self.max_file_size = 1024
        self.min_retention = 10
        self.max_retention = 360
        self.base_url = 'https://x0.at'

    def __calc_retention_date__(self, file: File) -> datetime:
        retention = int(self.min_retention + (
                self.max_retention - self.min_retention
        ) * int(1 - (file.file_size / self.max_retention)) ^ 2)
        if retention < self.min_retention:
            retention = self.min_retention
        return datetime.datetime.utcnow() + datetime.timedelta(days=retention)

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
            url=req.text.split('\n')[0],
            retention_to=self.__calc_retention_date__(file)
        )
