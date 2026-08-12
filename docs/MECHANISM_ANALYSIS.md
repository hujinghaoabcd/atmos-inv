# 2D vs 3D 反演偏差机制分析

这是项目从“方法论文”升级为“科学发现”的核心部分。

## 1. 主要响应变量

定义后验差异，例如：

```text
DeltaE = E_post_3D - E_post_2D
RelativeBias = DeltaE / (E_prior + eps)
```

也可比较 satellite residual、独立 ground residual 与 transport attribution。

## 2. 机制变量

优先物理变量而非大量社会经济特征：
- PBLH；
- PBLH tendency；
- vertical wind shear；
- wind-direction shear；
- vertical velocity/mixing proxy；
- stability；
- terrain relief；
- upwind emission burden；
- trajectory/transport distance；
- coastal/basin indicator；
- radiation/photochemical regime。

## 3. 分析层次

### Event level
典型输送过程做 case study：三维 plume、column、posterior 差异。

### Regime level
将 atmosphere 按少数可解释 regime 分类，比较 2D bias distribution。

### National level
建立全国空间规律，检查是否跨区域重复。

## 4. 统计设计

避免把上百万网格点当独立样本。需要考虑：
- spatial autocorrelation；
- repeated days；
- region fixed/random effects；
- block bootstrap；
- event-level aggregation。

## 5. 目标结果形式

理想结果不是“PBLH 与 bias 的 Pearson r=0.4”，而是类似：

> 当边界层内外风向差异和垂直交换达到某种 regime 时，2D 反演倾向把 downwind column enhancement 归因于 local emissions；该现象在多个区域可重复。

## 6. 反例同样重要

需要明确哪些条件下 2D approximation 足够：
- weak vertical shear；
- well-mixed boundary layer；
- local-dominant plume；
- low transport complexity。

最终结论应给出“什么时候需要 3D”，而不是宣称 3D 永远更好。
