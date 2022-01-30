import requests

from dataclasses import dataclass
from typing import Optional
from TemporaryStorage.providers import Provider, File, HostedFile


@dataclass
class ProviderInstance(Provider):
    def __provider_init__(self):
        self.provider = 'Telegraph'
        self.max_file_size = 50
        self.min_retention = None
        self.max_retention = None
        self.base_url = 'https://telegra.ph'

    def check_file(self, file: File) -> bool:
        if not (file.path.endswith('.jpg') or
                file.path.endswith('.jpeg') or
                file.path.endswith('.png') or
                file.path.endswith('.gif') or
                file.path.endswith('.mp4')):
            return False
        if file.file_size > self.max_file_size:
            return False

        return True

    def upload(self, file: File) -> Optional[HostedFile]:
        req = requests.post(self.base_url + '/upload', files={"file": open(file.path, 'rb')})

        if req.status_code != 200:
            return

        return HostedFile(
            provider=self.provider,
            url=self.base_url + req.json()[0]['src'],
            retention_to=None
        )
