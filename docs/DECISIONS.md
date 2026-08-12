# Architecture / Research Decision Record

本文件记录会影响科学解释、数据兼容性或复现性的决策。

## ADR-001 — 单仓库研究实验架构
**状态：FROZEN**

选择一个 `atmos-inv` 主仓库管理代码、配置、workflow、实验和论文证据；TB 级数据外置。

原因：保持从 paper → experiment → config → data provenance 的单一链路。

## ADR-002 — 全国主尺度 + 区域 refinement
**状态：REFERENCE DEFAULT**

全国主实验 12 km；重点区域 3–6 km。

最终 WRF domain geometry 在 benchmark 后冻结。

## ADR-003 — 主反演参数为 prior multiplicative correction
**状态：REFERENCE DEFAULT**

`E_post = E_prior * exp(log_alpha)`。

不从零直接生成绝对 emission。

## ADR-004 — TROPOMI 主反演使用 L2 native observation space
**状态：FROZEN IN PRINCIPLE**

避免先插值成固定 Level-3 图再训练/反演。

具体 AK/AMF handling 待产品版本审核。

## ADR-005 — 必须做 emission-intervention teacher
**状态：FROZEN**

固定历史排放训练不能作为唯一 teacher design，因为项目需要可靠 `dC/dE`。

## ADR-006 — Jacobian gate
**状态：FROZEN**

未通过 sensitivity fidelity 的神经模型不得进入真实 satellite inversion。

## ADR-007 — operator splitting
**状态：REFERENCE DEFAULT**

优先 transport graph + local chemistry operator，而不是一个 black-box GNN 包办全部过程。

## OPEN-001 — WRF-Chem chem_opt
必须与 chemical IC/BC、emission speciation 一起决定。

## OPEN-002 — WRF projection/domain dimensions
需小规模性能和边界输送设计后冻结。

## OPEN-003 — spin-up duration
需 diagnostics。

## OPEN-004 — vertical aggregation
fixed-pressure vs PBL-relative。

## OPEN-005 — intervention design
factorial / LHS / active learning。

## OPEN-006 — posterior uncertainty representation
先完成 deterministic inversion，再决定 ensemble/variational。

## ADR 模板

```text
ADR-NNN — title
Date:
Status:
Context:
Options:
Decision:
Evidence:
Consequences:
Affected configs/code:
```
