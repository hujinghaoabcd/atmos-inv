# Contributing to AtmosInv

AtmosInv is a research repository. Scientific traceability has priority over rapid code accumulation.

## Before implementing a feature

1. Identify the corresponding design document.
2. Identify or create an Experiment ID if scientific results will be produced.
3. Do not silently freeze an `OPEN` scientific decision in code.
4. Add tests for units, shapes, mappings, or gradients where relevant.

## Pull-request expectations

A scientific implementation PR should state:
- question addressed;
- affected config groups;
- data/teacher assumptions;
- validation performed;
- experiment IDs enabled;
- changes to reproducibility/provenance;
- documentation updated.

## Large files

Do not commit atmospheric data, WRF outputs, checkpoints, or credentials. The pre-commit large-file check is only a safety net, not the storage policy.

## Notebooks

Notebooks may be used for exploration, but production transformations, metrics, and paper figures must migrate into `src/`, `scripts/`, or reproducible workflow rules before they become paper evidence.
