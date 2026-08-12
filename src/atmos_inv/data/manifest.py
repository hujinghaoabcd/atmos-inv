"""Minimal immutable metadata objects for external scientific datasets."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class DatasetManifest:
    dataset_id: str
    product: str
    version: str
    start_date: str
    end_date: str
    spatial_scope: str
    source: str
    checksum_index: str | None = None
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
