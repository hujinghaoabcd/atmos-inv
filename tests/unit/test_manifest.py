from atmos_inv.data.manifest import DatasetManifest


def test_manifest_round_trip_dict() -> None:
    manifest = DatasetManifest(
        dataset_id="SAT-TROP-NO2",
        product="L2_NO2",
        version="example",
        start_date="2021-01-01",
        end_date="2021-01-02",
        spatial_scope="test",
        source="official-source",
    )
    payload = manifest.to_dict()
    assert payload["dataset_id"] == "SAT-TROP-NO2"
    assert payload["checksum_index"] is None
