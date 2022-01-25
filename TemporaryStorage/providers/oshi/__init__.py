import datetime
import requests

from dataclasses import dataclass
from typing import Optional
from TemporaryStorage.providers import Provider, File, HostedFile


@dataclass
class ProviderInstance(Provider):
    def __provider_init__(self):
        self.provider = 'oshi.at'
        self.max_file_size = 5000
        self.min_retention = 7
        self.max_retention = 90
        self.base_url = 'https://oshi.at'

    def __calc_retention_date__(self, file: File) -> datetime:
        return datetime.datetime.utcnow() + datetime.timedelta(days=round(self.__calc_retention_period__(file)) - 1)

    def __calc_retention_period__(self, file: File) -> int:
        retention = int(self.min_retention + (
                -self.max_retention + self.min_retention
        ) * pow((file.file_size / self.max_retention - 1), 3))
        if retention < self.min_retention:
            retention = self.min_retention
        return retention

    def check_file(self, file: File) -> bool:
        if file.file_size > self.max_file_size:
            return False

        return True

    def upload(self, file: File) -> Optional[HostedFile]:
        retention_period = self.__calc_retention_period__(file)

        req = requests.post(self.base_url,
                            files={"file": open(file.path, 'rb')},
                            data={"expire": retention_period * 1440})

        if req.status_code != 200:
            return

        if 'DL: ' not in req.text:
            return

        return HostedFile(
            provider=self.provider,
            url=req.text.split('DL: ')[1].split('\n')[0],
            retention_to=self.__calc_retention_date__(file)
        )

