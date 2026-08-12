# 文献地图与后续检索任务

本文件只记录研究邻域和锚点，不在项目冻结期假装完成最终 systematic review。正式论文写作前需要重新检索最新原始文献并核对 DOI、版本和 novelty。

## 1. Satellite NOx emission inversion

关注：
- mass-balance / flux-divergence；
- Bayesian/variational/ensemble inversion；
- high-resolution urban/power-plant inversion；
- daily national-scale inversion；
- prior dependence and identifiability。

已知锚点方向：TROPOMI NO2 城市/电厂定量、PHLET/continuity approaches、DECSO/CIF/LETKF 等。

## 2. Physics + AI inversion

重点：
- differentiable transport/chemistry decoder；
- PINE-like emission inversion；
- PINN source inversion；
- neural surrogate + Bayesian inversion。

必须回答：已有工作是否显式三维？是否保持 `dC/dE`？是否直接进入真实 satellite inversion？

## 3. Atmospheric transport emulators

锚点：
- FootNet 系列；
- GATES graph-neural atmospheric transport；
- neural global tracer transport studies。

比较维度：2D footprint vs 3D state、passive tracer vs reactive chemistry、regional vs global、forward-only vs inverse use。

## 4. Weather / Earth-system foundation operators

锚点：
- GraphCast；
- Pangu-Weather；
- NeuralGCM；
- Aurora；
- regional AI limited-area models。

本项目借鉴：multiscale state evolution / hybrid physics / pretrain-downstream，而不是参数规模。

## 5. WRF-Chem + satellite + ML

重点关注：
- WRF-Chem synthetic profiles + TROPOMI；
- ML profile reconstruction；
- air-quality neural CTM；
- model bias correction vs true operator learning。

## 6. Dynamic atmospheric GNN

检索：wind-directed graphs、advection-diffusion graph learning、physics-inspired air-quality GNN。

目的：避免将“动态风图”错误包装为独立 novelty。

## 7. 文献矩阵字段

正式建立 `literature.csv` 时至少记录：

```text
title
year
journal
study_region
species
observations
forward_model
inverse_method
spatial_scale
temporal_scale
3d_transport
chemistry
learned_operator
sensitivity_validation
satellite_operator
independent_validation
key_novelty
limitation
relation_to_atmosinv
```

## 8. 启动前检索问题

1. 2026 年是否已有完全相同的 3D differentiable graph CTM + TROPOMI NOx inversion？
2. 是否已有工作系统比较 2D vs 3D satellite NOx inversion bias？
3. 是否已有 neural surrogate 明确验证 Jacobian/sensitivity，而不仅是 state RMSE？
4. 最新 TROPOMI/GEMS product algorithm 有何变化？
5. 最新全国 MEIC/中国排放产品是否更新到更近年份？
