# TROPOMI Satellite Observation Operator

## 1. 为什么单独作为模块

模型输出是三维 NO2 state；TROPOMI 提供的是具有像元 footprint、垂直敏感性和 retrieval assumptions 的柱观测。两者不能通过“把卫星插值到 12 km 网格”简单等同。

## 2. 基本映射

逻辑上：

```text
model mixing ratio / concentration
→ pressure/height layer mapping
→ partial column
→ satellite vertical sensitivity / AK treatment
→ horizontal pixel overlap integration
→ predicted L2 observation
```

具体公式必须按照实际使用的 TROPOMI NO2 产品版本、变量定义和官方 ATBD/PUM 冻结，禁止根据记忆写死。

## 3. Horizontal observation operator

对于每个真实卫星像元 `p`：

```text
y_hat_p = sum_i overlap_weight[p, i] * column_i
```

权重来自真实 pixel polygon 与模型 cell 的面积重叠，考虑投影/球面面积一致性。

## 4. Vertical mapping

需要处理：
- model vertical coordinates；
- satellite pressure grid；
- surface pressure difference；
- tropopause definition；
- averaging kernel；
- AMF/retrieval convention。

不同 comparison convention（应用 AK 到 model 还是重算某些量）必须在文献与产品文档基础上确定，并用已知 benchmark 验证。

## 5. QA / cloud

QA 阈值不硬编码在算法内部；作为 versioned config。需要 sensitivity：
- strict QA；
- relaxed QA；
- cloud fraction thresholds。

## 6. 时间匹配

不能直接拿每日平均 model state 对 13:30 左右过境。应按像元 observation time 对小时状态进行最近邻或时间插值，并记录 temporal mismatch。

## 7. Loss weighting

候选权重：
- inverse observation variance；
- quality-aware weight；
- uniform baseline。

避免让高 NO2 城市像元因绝对误差大完全支配 loss；同时避免相对误差在低背景区爆炸。需要多指标共同评估。

## 8. 验收测试

在接入反演前必须完成：
- synthetic column test；
- uniform profile analytical test；
- overlap area conservation；
- pressure-grid mapping test；
- selected real-orbit hand check；
- 与独立成熟 comparison code/文献 workflow 对照（如可获得）。
