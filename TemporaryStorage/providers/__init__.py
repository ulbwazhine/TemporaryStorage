import os

from dataclasses import dataclass, field
from pathlib import Path
from datetime import datetime
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


def default_factory_false() -> bool:
    return False


@dataclass(frozen=False)
class File:
    provider: Optional[str] = field(default_factory=default_factory_none)
    name: Optional[str] = field(default_factory=default_factory_none)
    path: Optional[str] = field(default_factory=default_factory_none)
    url: Optional[str] = field(default_factory=default_factory_none)
    file_size: Optional[float] = field(default_factory=default_factory_none)
    retention_to: Optional[datetime] = field(default_factory=default_factory_none)


@dataclass(frozen=False)
class Provider:
    provider: str = field(default_factory=str)
    max_file_size: int = field(default_factory=int)
    base_url: str = field(default_factory=str)

    def __post_init__(self):
        getattr(self, '__provider_init__')()
