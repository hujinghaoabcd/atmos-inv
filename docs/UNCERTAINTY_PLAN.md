# 不确定性分析计划

## 1. 不确定性来源

至少区分：
- satellite retrieval uncertainty；
- prior emission uncertainty；
- meteorological uncertainty；
- chemistry/teacher structural uncertainty；
- neural approximation uncertainty；
- inversion regularization uncertainty；
- sampling/episode uncertainty。

不要把 neural seed variance 当成“总不确定性”。

## 2. 第一阶段可实现层次

### U1 Neural ensemble
多个 seed/architecture perturbations。

### U2 Observation weighting sensitivity
retrieval precision、QA、cloud threshold。

### U3 Prior sensitivity
不同 prior strength / selected inventory alternatives。

### U4 Teacher structural sensitivity
有限 PBL/chemistry configurations 或关键 episode sensitivity。

### U5 Bootstrap
按 day/event/region block bootstrap，而不是网格点独立 bootstrap。

## 3. Posterior uncertainty

第一篇不强制完整 Bayesian posterior。可先提供：
- ensemble spread；
- prior/regularization sensitivity envelope；
- observation uncertainty propagation experiments；
- robust mechanism intervals。

如果要声称 emission magnitude 的 formal uncertainty，再升级 ensemble/variational Bayesian design。

## 4. Mechanism uncertainty

最终 `2D bias = f(regime)` 需要报告：
- confidence interval；
- region-to-region heterogeneity；
- event bootstrap；
- alternate regime definition sensitivity。
