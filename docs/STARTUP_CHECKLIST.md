# 项目正式启动检查表

> 项目长期暂停后，不要直接从“下载三年数据”开始。按本表顺序重新进入。

## Phase 0 — Re-validate assumptions

- [ ] 阅读 `PROJECT_OVERVIEW.md`
- [ ] 阅读 `DECISIONS.md`
- [ ] 更新 `STATUS.md`
- [ ] 检索 2026 年之后相关论文，更新 novelty
- [ ] 核对 TROPOMI NO2 最新/历史 reprocessing 产品
- [ ] 核对 GEMS 产品版本
- [ ] 核对 MEIC/中国 emission inventory 是否有新版本
- [ ] 确定计算平台/HPC
- [ ] 确定 permanent + scratch storage

## Phase 1 — Environment

- [ ] 冻结 Python 版本
- [ ] 安装 bootstrap tests
- [ ] `pytest`
- [ ] `python scripts/check_project.py`
- [ ] 配置 `ATMOSINV_*_ROOT`
- [ ] 记录 WRF-Chem compiler/MPI/NetCDF stack

## Phase 2 — Small data samples only

- [ ] 下载 1–2 个 TROPOMI orbit
- [ ] 检查实际 NetCDF variable names/dimensions
- [ ] 下载 2–3 天 ERA5
- [ ] 获取 MEIC sample
- [ ] WPS geography
- [ ] 地面站 sample + metadata
- [ ] 建立 first manifests/checksums

Exit gate：真实数据 schema 已经验证。

## Phase 3 — Freeze WRF-Chem pathway

- [ ] 选择 `chem_opt`
- [ ] 确定 chemical IC/BC
- [ ] 确定 emission speciation
- [ ] 冻结 domain projection
- [ ] 6 h run
- [ ] 24 h benchmark
- [ ] meteorological sanity
- [ ] chemical sanity
- [ ] GB/day 和 wall-clock/day benchmark

## Phase 4 — Teacher pilot

- [ ] baseline episode
- [ ] +25% NOx intervention
- [ ] -25% NOx intervention
- [ ] 检查 response
- [ ] vertical aggregation pilot
- [ ] teacher schema/chunk benchmark

## Phase 5 — Model pilot

- [ ] synthetic graph tests
- [ ] real teacher slice
- [ ] 1-step forward
- [ ] emission-input ablation
- [ ] neural finite difference

## Phase 6 — Scale-up decision

只有在前五阶段通过后，决定：
- [ ] episode 数量
- [ ] intervention design
- [ ] nationwide production runs
- [ ] regional refinement
- [ ] storage expansion

## Phase 7 — Satellite inversion

必须先通过 E320/E330 Jacobian gate。

- [ ] native-pixel observation operator tests
- [ ] twin inversion
- [ ] small real region inversion
- [ ] national daily inversion

## Phase 8 — Paper mode

- [ ] freeze experiment matrix
- [ ] execute E9xx reproduction
- [ ] update evidence map
- [ ] archive configs/manifests
