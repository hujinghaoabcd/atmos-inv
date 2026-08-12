# 项目路线图

## M0 — Bootstrap / Design Freeze（当前）

目标：项目未启动也不会丢失设计。

- [x] repository skeleton
- [x] config hierarchy
- [x] experiment IDs
- [x] scientific design docs
- [x] data plan
- [x] algorithm interfaces
- [x] risk/reproducibility plan
- [ ] final literature verification
- [ ] choose license

## M1 — Data Foundation

- [ ] verify product versions
- [ ] download small samples
- [ ] implement manifests/checksum
- [ ] TROPOMI reader/schema
- [ ] ERA5 workflow
- [ ] emission inventory audit
- [ ] ground station metadata

Exit gate：所有核心 raw data 均有小样本 + schema + provenance。

## M2 — WRF-Chem Teacher

- [ ] compile/validate target WRF-Chem
- [ ] freeze domain/physics/chemistry
- [ ] 24 h benchmark
- [ ] representative episodes
- [ ] intervention pilot
- [ ] teacher_v1

## M3 — Neural Operator

- [ ] synthetic 3D graph
- [ ] real teacher slice
- [ ] 1-step training
- [ ] rollout
- [ ] dynamic/vertical/multiscale graph
- [ ] chemistry operator

## M4 — Sensitivity Gate

- [ ] neural finite differences
- [ ] autograd check
- [ ] CTM Jacobian comparison
- [ ] unseen interventions

失败则禁止进入 real inversion。

## M5 — Satellite Inversion

- [ ] TROPOMI observation operator
- [ ] twin inversion
- [ ] daily China inversion
- [ ] prior/QA sensitivity
- [ ] independent validation

## M6 — Scientific Mechanism

- [ ] 2D vs 3D
- [ ] atmospheric regime analysis
- [ ] cross-region generalization
- [ ] regional refinement

## M7 — Paper / Archive

- [ ] freeze configs/data versions
- [ ] E9xx reproduction
- [ ] figures/tables provenance
- [ ] documentation audit
- [ ] archive/tag/release
