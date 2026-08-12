# Workflow / HPC 执行设计

## 1. 职责划分

Hydra：参数组合和 resolved config。

Snakemake：任务依赖、输入输出、重跑判定、HPC orchestration。

SLURM/PBS：资源调度。

WRF-Chem：外部 compiled teacher。

MLflow：未来记录神经模型 run；不替代 experiment registry。

## 2. 目标 workflow

```text
data_audit
→ wrf_input
→ wrfchem_baseline
→ wrfchem_interventions
→ teacher_extract
→ teacher_release
→ graph_cache
→ train_operator
→ jacobian_gate
→ satellite_match
→ twin_inversion
→ real_inversion
→ validation
→ mechanism
→ paper_reproduce
```

## 3. Job granularity

WRF-Chem：每 episode/intervention 独立 job，可 restart。

Preprocessing：按 episode/time chunk。

ML：按 seed/config 独立 run。

Inversion：按 day/window/region 分片，但需要明确跨窗口 chemical state handling。

## 4. Failure-safe

- job completion marker 只在 QA 通过后生成；
- partial NetCDF 不作为有效 input；
- restart 与 clean start 明确区分；
- checksum/size sanity；
- Snakemake `protected()` 用于高成本稳定产物；
- scratch 清理必须依赖 archive marker。

## 5. Resource profiles

未来建立：

```text
profiles/slurm/
profiles/local/
profiles/workstation/
```

不要把具体 partition/account 写入通用 Snakefile。

## 6. Dry run

任何 production workflow 必须支持：

```bash
snakemake -n ...
```

先检查 DAG 再提交 HPC。
