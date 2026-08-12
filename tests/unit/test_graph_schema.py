import pytest

from atmos_inv.graph.schema import AtmosphericGraphSpec


def test_reference_graph_spec_is_valid() -> None:
    AtmosphericGraphSpec(
        horizontal_resolution_km=12,
        vertical_layers=6,
        multiscale_levels_km=(12, 36, 108),
    ).validate()


def test_invalid_vertical_layer_count_rejected() -> None:
    with pytest.raises(ValueError):
        AtmosphericGraphSpec(horizontal_resolution_km=12, vertical_layers=0).validate()
