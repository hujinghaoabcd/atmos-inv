# 论文叙事与投稿计划

## 1. 论文中心句

优先科学叙事：

> Explicitly resolving three-dimensional atmospheric transport changes how satellite NO2 columns are attributed to surface NOx emissions under identifiable boundary-layer and transport regimes.

神经算子是实现全国/多实验反演的 enabling method，而不是论文唯一主角。

## 2. 暂定标题方向

### 方法导向
**A 3D graph neural chemistry–transport operator for satellite-constrained NOx emission inversion**

### 科学问题导向
**Three-dimensional atmospheric transport reshapes satellite-derived NOx emission attribution over China**

### 综合导向
**Learning three-dimensional atmospheric transport for satellite-constrained NOx emission inversion across China**

标题在看到 E5xx 结果后再定。

## 3. Introduction 逻辑

1. 排放清单对空气质量和政策重要；
2. satellite top-down inversion 能独立约束排放；
3. 但 column observation 到 surface source 的映射依赖 transport/vertical mixing/chemistry；
4. 高保真 CTM inversion 昂贵，简化 transport 可能引入 attribution bias；
5. neural atmospheric operators 提供可微、快速的 forward model；
6. 关键未知不是“AI 是否预测得准”，而是能否保持 emission sensitivity 并揭示 3D transport 对 inversion 的系统影响。

## 4. Results 章节候选

1. **A neural operator that preserves atmospheric state evolution**；
2. **Emission-intervention training recovers CTM sensitivity**；
3. **Satellite-constrained posterior NOx emissions over China**；
4. **When 2D inversion misattributes transported NO2**；
5. **Cross-region generality and limits of the mechanism**。

## 5. 期刊层级策略

- 方法/模型扎实：GMD/JAMES/ACP 类；
- 强排放发现与独立证据：ES&T/RSE 类；
- 强 Scientific AI + 大气机制：npj Climate and Atmospheric Science；
- 全国/跨区域普适科学规律非常强：再考虑 Nature Communications 等。

投稿目标最终由科学结果决定，不在项目启动前锁死。

## 6. 论文中不要做的事

- 把所有提升都归因于 GNN；
- 宣称“首次”而没有系统检索；
- 只报平均 RMSE；
- 把 satellite fit 当 posterior truth；
- 隐藏 prior regularization；
- 只展示几个漂亮 case；
- 用过度复杂模型名掩盖简单科学问题。
