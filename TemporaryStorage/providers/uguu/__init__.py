import datetime
import requests

from dataclasses import dataclass
from typing import Optional
from TemporaryStorage.providers import Provider, File


@dataclass
class ProviderInstance(Provider):
    def __provider_init__(self):
        self.provider = 'uguu.se'
        self.max_file_size = 100
        self.base_url = 'https://uguu.se'

    @staticmethod
    def calc_retention_date(file: File) -> datetime:
        return datetime.datetime.utcnow() + datetime.timedelta(hours=48)

    def check_file(self, file: File) -> bool:
        if file.file_size > self.max_file_size:
            return False

        return True

    def upload(self, file: File) -> Optional[File]:
        req = requests.post(self.base_url + '/upload.php', files={"files[]": open(file.path, 'rb')})

        if req.status_code != 200:
            return

        if not req.json().get('success'):
            return

        file.provider = self.provider
        file.url = req.json().get('files', [])[-1].get('url')
        file.retention_to = self.calc_retention_date(file)

        if not file.url:
            return

        return file
