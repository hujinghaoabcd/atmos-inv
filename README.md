# AtmosInv

**Satellite-constrained 3D graph neural atmospheric operator for national-scale NOx emission inversion**

> **Project state:** design and preparation. The scientific plan, data contracts, model interfaces, experiment registry, and reproducibility workflow are prepared in advance; production data download and large-scale WRF-Chem experiments have **not** started.

AtmosInv is a research-experiment repository for studying whether explicitly resolving three-dimensional atmospheric transport changes satellite-derived NOx emission estimates, and for building a differentiable neural chemistry–transport operator that can support TROPOMI-constrained inversion at national scale.

The repository is intentionally designed as a **single evidence chain** rather than a collection of disconnected scripts:

```text
Scientific question
      ↓
Data provenance
      ↓
WRF-Chem teacher simulations
      ↓
Emission-intervention ensemble
      ↓
3D atmospheric graph / neural operator
      ↓
Satellite observation operator
      ↓
Differentiable NOx inversion
      ↓
Independent validation
      ↓
2D-vs-3D mechanism analysis
      ↓
Paper figures / tables
```

## Scientific hypothesis

The project tests the hypothesis that 2D or near-surface transport approximations can systematically misattribute transported NO2 columns to local surface emissions under specific boundary-layer, vertical-mixing, wind-shear, and terrain regimes. A 3D atmospheric neural operator is used not merely as a faster predictor, but as a differentiable forward model whose **emission sensitivity** can be validated and then used in inverse modeling.

A central requirement is therefore not only

```text
C_neural ≈ C_WRF-Chem
```

but also

```text
∂C_neural / ∂E ≈ ∂C_WRF-Chem / ∂E
```

before the learned operator is trusted for emission inversion.

## Planned scope

The current reference design is:

- **Main domain:** China-wide domain with transport buffer.
- **Reference national resolution:** 12 km.
- **Regional refinement:** 3–6 km over representative regions such as the North China Plain, Yangtze River Delta, Pearl River Delta, and Sichuan Basin.
- **WRF-Chem:** full native vertical structure for teacher simulations.
- **Neural operator:** compressed physically meaningful vertical representation, initially 6–8 layers.
- **Forward temporal resolution:** hourly.
- **Primary satellite:** Sentinel-5P/TROPOMI Level-2 tropospheric NO2.
- **Primary inversion target:** daily posterior NOx emission correction factors.
- **Primary prior:** MEIC-based anthropogenic emissions, with external-domain emissions supplied by an appropriate global inventory.
- **Optional extension:** GEMS daytime hourly NO2 for sub-daily inversion and validation.
- **Reference analysis period:** 2021–2023; representative seasonal episodes are expected to be used for expensive chemistry-transport teacher simulations.

All values above are **design defaults, not immutable scientific facts**. Frozen decisions and unresolved decisions are tracked in `docs/DECISIONS.md`.

## Repository philosophy

Git stores **code, configuration, metadata, manifests, and paper evidence**. Large atmospheric data do not live in Git.

```text
Git/GitHub            → code, docs, experiment definitions, CI, provenance
Hydra                 → parameter composition and resolved experiment configs
Snakemake             → workflow DAG and compute orchestration
WRF-Chem              → physics/chemistry teacher simulations
PyTorch / PyG         → neural atmospheric operator
MLflow (planned)      → ML run metrics and model artifacts
External storage      → TROPOMI, ERA5, emissions, WRF-Chem outputs, teacher datasets
```

Every publishable result should ultimately be traceable through:

```text
Paper figure/table
  → Experiment ID
  → Run ID
  → Resolved Hydra config
  → Git commit SHA
  → Teacher dataset version
  → WRF-Chem run IDs
  → Data manifests/checksums
```

## Top-level structure

```text
atmos-inv/
├── configs/          # Hydra configuration hierarchy
├── docs/             # scientific design, protocols, decisions, roadmap
├── experiments/      # experiment registry and immutable manifests
├── src/atmos_inv/    # reusable Python research code
├── workflows/        # Snakemake workflow and stage rules
├── scripts/          # project utilities and entry points
├── tests/            # unit, integration, and smoke tests
├── environment/      # environment guidance
└── .github/          # CI and issue templates
```

See **`docs/README.md`** for the full documentation map.

## Current implementation status

The repository is currently in **M0 — Bootstrap / Design Freeze**. The goal of this phase is to make the future project executable without rediscovering its assumptions months later.

Prepared in this phase:

- repository architecture;
- configuration hierarchy;
- external path contract;
- data catalog and download plan;
- WRF-Chem protocol skeleton;
- emission-intervention teacher design;
- 3D graph/operator algorithm specification;
- TROPOMI observation-operator specification;
- inversion objective and constraints;
- Jacobian/emission-sensitivity validation protocol;
- experiment matrix and ID convention;
- geographic generalization and ablation plans;
- storage/compute planning;
- risk register and fallback designs;
- paper outline and evidence requirements;
- restart/handoff checklist.

## Quick bootstrap

The large-scale scientific workflow is intentionally disabled at this stage. The repository can still be installed and its lightweight tests can be run:

```bash
python -m venv .venv
# activate the environment
pip install -e ".[dev]"
pytest
```

Hydra configuration composition can later be inspected without running atmospheric simulations:

```bash
python -m atmos_inv.cli --help
```

## Data policy

Do **not** commit raw or processed atmospheric datasets, WRF/WRF-Chem outputs, model checkpoints, or inversion products to Git. Use external roots configured through environment variables and manifests. See:

- `docs/DATA_CATALOG.md`
- `docs/DATA_DOWNLOAD_PLAN.md`
- `docs/REPRODUCIBILITY.md`

## Documentation entry points

Start with:

1. `docs/PROJECT_OVERVIEW.md` — end-to-end project definition.
2. `docs/SCIENTIFIC_QUESTIONS.md` — hypotheses and falsifiable questions.
3. `docs/INNOVATION.md` — what is and is not claimed as novelty.
4. `docs/SYSTEM_ARCHITECTURE.md` — full data/model/inversion architecture.
5. `docs/EXPERIMENT_MATRIX.md` — formal experiment families.
6. `docs/STARTUP_CHECKLIST.md` — what to do when the project is activated.

## Development rule

No number enters a paper because it “looked good in a notebook.” A result is considered paper-eligible only when its experiment ID, resolved configuration, code version, data/teacher provenance, and evaluation script are recoverable.

## License

A project license has **not yet been selected**. Do not assume reuse rights beyond GitHub's default viewing/forking behavior until a license decision is recorded.
