# Environment strategy

AtmosInv deliberately separates the **Python research environment** from the **WRF/WRF-Chem compiled environment**.

- Python: configuration, preprocessing, graph/operator training, inversion, evaluation.
- WRF-Chem: compiled and validated independently on the target HPC system.
- Do not attempt to force WRF-Chem, MPI, NetCDF-C/Fortran, and the Python ML stack into one environment.

For local repository checks:

```bash
pip install -e ".[dev]"
pytest
```

For future full Python work:

```bash
pip install -e ".[data,geo,ml,workflow,tracking,dev]"
```

A cluster-specific environment lock should be created only when the actual compute platform is selected. Record compiler, MPI, NetCDF, HDF5, WRF, WPS, WRF-Chem, CUDA, PyTorch and PyG versions in every production run manifest.
