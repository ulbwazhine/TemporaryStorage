import logging
import os
import random

from importlib import import_module
from typing import List, Optional
from TemporaryStorage import providers
from TemporaryStorage.providers import File


class TemporaryStorageInstance:
    def __init__(self):
        self.logger = logging.getLogger('TemporaryStorage')
        self.providers: List[providers.Provider] = []

        for provider in providers.ALL_PROVIDERS:
            self.providers.append(getattr(
                import_module(name='TemporaryStorage.providers.' + provider,
                              package='TemporaryStorage.providers.' + provider + '.ProviderInstance'),
                'ProviderInstance')())

    def __create_providers_list__(self) -> str:
        output = list()

        for provider in self.providers:
            output.append(
                '* [{provider}]({base_url}) [up to {max_file_size} MB]'.format(
                    provider=provider.provider, base_url=provider.base_url,
                    max_file_size=provider.max_file_size))

        return '\n'.join(output)

    def upload(self, path: str) -> Optional[File]:
        file = File(name=os.path.basename(path),
                    path=path,
                    file_size=round(os.path.getsize(path) / 1e+6, 1))

        random.shuffle(self.providers)

        for provider in self.providers:
            try:
                if not getattr(provider, 'check_file')(file):
                    continue

                uploaded = getattr(provider, 'upload')(file)

                if not uploaded:
                    continue
                else:
                    break
            except (Exception, BaseException):
                continue

        return file


