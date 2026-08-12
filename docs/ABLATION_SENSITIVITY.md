# 消融与敏感性实验

## 1. 原则

消融不是把所有模块逐个删一遍凑表格，而是回答：**哪个设计对 forward fidelity、emission sensitivity 和 inversion mechanism 分别重要？**

## 2. 图结构消融

- distance-only graph；
- static adjacency；
- wind-directed 2D graph；
- + vertical edges；
- + PBL/mixing features；
- + learned residual connectivity；
- + multiscale hierarchy。

## 3. 垂直表示

比较：
- 1 layer（2D baseline）；
- 3 layers；
- 6 layers；
- 8 layers；
- fixed pressure aggregation；
- PBL-relative aggregation。

## 4. Chemistry representation

- NO2 only；
- NO + NO2 + O3；
- extended reservoirs；
- no explicit chemistry block；
- local chemistry block。

## 5. Teacher design

- historical-only；
- global scaling only；
- spatial interventions；
- sector interventions；
- full intervention ensemble。

这是验证 emission-intervention pretraining 的关键消融。

## 6. Satellite operator

- crude model-grid resampling；
- native pixel horizontal overlap；
- + vertical mapping；
- + AK/AMF-consistent treatment。

用于量化 observation operator 自身对 posterior 的影响。

## 7. Inversion regularization

- prior strength；
- spatial smoothness；
- temporal smoothness；
- correction bounds/parameterization；
- observation uncertainty weighting。

## 8. Sensitivity output

每个敏感性实验记录：
- effect on main claim；
- effect size；
- confidence interval；
- whether qualitative conclusion changes。

如果主要机制结论只在某个任意超参数下成立，则不能作为稳健科学发现。
