import datetime
import requests

from dataclasses import dataclass
from typing import Optional
from TemporaryStorage.providers import Provider, File


@dataclass
class ProviderInstance(Provider):
    def __provider_init__(self):
        self.provider = 'x0.at'
        self.max_file_size = 1024
        self.base_url = 'https://x0.at'

    @staticmethod
    def calc_retention_date(file: File) -> datetime:
        retention = 10 + (360 - 10) * int(1 - (file.file_size / 360)) ^ 2
        if retention < 10:
            retention = 10
        return datetime.datetime.utcnow() + datetime.timedelta(days=int(retention) - 1)

    def check_file(self, file: File) -> bool:
        if file.file_size > self.max_file_size:
            return False

        return True

    def upload(self, file: File) -> Optional[File]:
        req = requests.post(self.base_url,
                            files={"file": open(file.path, 'rb')})

        if req.status_code != 200:
            return

        file.provider = self.provider
        file.url = req.text.split('\n')[0]
        file.retention_to = self.calc_retention_date(file)

        return file
