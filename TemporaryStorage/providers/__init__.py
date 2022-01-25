import os

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

providers_path = os.path.join("/".join(os.path.dirname(os.path.abspath(__file__)).split('/')[:-1]), 'providers')


def __list_all_providers():
    all_templates = [x.name for x in Path(providers_path).iterdir()
                     if x.is_dir() and not str(x).startswith('__') and not str(x).endswith('__')]
    return all_templates


ALL_PROVIDERS = sorted(__list_all_providers())
__all__ = ALL_PROVIDERS + ["ALL_PROVIDERS"]


def default_factory_none() -> None:
    return None


@dataclass(frozen=False)
class File:
    name: str = field()
    path: str = field()
    file_size: float = field()


@dataclass(frozen=False)
class HostedFile:
    provider: str = field()
    url: str = field()
    retention_to: Optional[datetime] = field()


@dataclass(frozen=False)
class Provider:
    provider: str = field(default_factory=default_factory_none)
    max_file_size: Optional[int] = field(default_factory=default_factory_none)
    min_retention: Optional[int] = field(default_factory=default_factory_none)
    max_retention: Optional[int] = field(default_factory=default_factory_none)
    base_url: str = field(default_factory=default_factory_none)

    def __post_init__(self):
        getattr(self, '__provider_init__')()
