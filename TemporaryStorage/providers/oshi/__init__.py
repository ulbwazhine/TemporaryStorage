import datetime
import requests

from dataclasses import dataclass
from typing import Optional
from TemporaryStorage.providers import Provider, File


@dataclass
class ProviderInstance(Provider):
    def __provider_init__(self):
        self.provider = 'oshi.at'
        self.max_file_size = 5000
        self.base_url = 'https://oshi.at'

    def calc_retention_date(self, file: File) -> datetime:
        return datetime.datetime.utcnow() + datetime.timedelta(days=round(self.calc_retention_period(file)) - 1)

    @staticmethod
    def calc_retention_period(file: File) -> int:
        return round(7 + (-90 + 7) * pow((file.file_size / 90 - 1), 3))

    def check_file(self, file: File) -> bool:
        if file.file_size > self.max_file_size:
            return False

        return True

    def upload(self, file: File) -> Optional[File]:
        retention_period = self.calc_retention_period(file)

        req = requests.post(self.base_url,
                            files={"file": open(file.path, 'rb')},
                            data={"expire": retention_period * 1440})

        if req.status_code != 200:
            return

        if 'DL: ' not in req.text:
            return

        file.provider = self.provider
        file.url = req.text.split('DL: ')[1].split('\n')[0]
        file.retention_to = self.calc_retention_date(file)

        return file
