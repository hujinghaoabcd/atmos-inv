# 论文证据映射（预设计）

本文档提前定义“想写什么结论，需要什么实验支撑”，防止结果出来后选择性拼故事。

## Figure 1 — Concept / architecture
来源：设计图，不作为性能证据。

## Figure 2 — Forward operator fidelity
需要：E200–E250。
- map/profile/column；
- rollout；
- regimes。

## Figure 3 — Emission sensitivity
需要：E300–E330。
- CTM vs neural Jacobian；
- historical-only vs intervention；
- downwind/vertical response。

## Figure 4 — China posterior emissions
需要：E420 + prior sensitivity。
- prior/posterior；
- uncertainty；
- independent validation。

## Figure 5 — 2D vs 3D mechanism
需要：E500–E540。
- national difference；
- regime dependence；
- representative cases。

## Figure 6 — Generalization
需要：E600–E650。
- leave-one-region-out；
- unseen weather；
- mechanism stability。

## Main Table 1
Forward baselines + proposed model，必须同时有 state 与 sensitivity metrics。

## Main Table 2
Posterior validation：satellite holdout + ground/column/independent evidence。

## Supplement
- hyperparameters；
- WRF-Chem validation；
- QA sensitivity；
- regularization sensitivity；
- vertical layer ablations；
- extra regions/events；
- data provenance。

## Evidence rule

任何 main-text claim 在写入论文前要在本文件补充：

```text
Claim ID
Experiment ID(s)
Run ID(s)
Figure/Table
Uncertainty
Known limitation
```
