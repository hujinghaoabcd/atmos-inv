"""Graph specification types shared by preprocessing and models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AtmosphericGraphSpec:
    horizontal_resolution_km: float
    vertical_layers: int
    dynamic_horizontal_edges: bool = True
    dynamic_vertical_edges: bool = True
    multiscale_levels_km: tuple[float, ...] = ()

    def validate(self) -> None:
        if self.horizontal_resolution_km <= 0:
            raise ValueError("horizontal_resolution_km must be positive")
        if self.vertical_layers < 1:
            raise ValueError("vertical_layers must be >= 1")
        if any(scale <= 0 for scale in self.multiscale_levels_km):
            raise ValueError("all multiscale levels must be positive")
