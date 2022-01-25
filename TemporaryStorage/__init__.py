import logging
import os
import random

from importlib import import_module
from typing import List, Optional
from TemporaryStorage import providers
from TemporaryStorage.providers import File, HostedFile


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
            file_size = (
                'Up to {} MB'.format(provider.max_file_size) if provider.max_file_size else 'Unlimited')

            retention_period = (('{} days'.format(provider.max_retention)
                                 ) if provider.max_retention == provider.min_retention and provider.max_retention else (
                ('From {} to {} days'.format(provider.min_retention, provider.max_retention)
                 ) if provider.max_retention else 'Unlimited'))

            output.append(
                '| [{provider}]({base_url}) | {file_size} | {retention_period} |'.format(
                    provider=provider.provider, base_url=provider.base_url,
                    file_size=file_size,
                    retention_period=retention_period))

        return '\n'.join(output)

    def upload(self, path: str) -> Optional[HostedFile]:
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
        else:
            uploaded = None

        return uploaded
