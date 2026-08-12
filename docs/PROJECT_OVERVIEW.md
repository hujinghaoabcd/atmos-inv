# 项目总体设计

## 1. 项目定位

AtmosInv 研究的不是“用一个更复杂的 GNN 预测 NO2”，而是建立一条可检验的科学链：

> **卫星柱浓度反演中，显式三维输送是否会系统性改变地表 NOx 排放归因？**

方法上构建一个由 WRF-Chem 教师模拟训练的、可微分的三维神经化学输送算子，再利用 TROPOMI Level-2 原始像元约束后验 NOx 排放。

## 2. 核心前向问题

定义三维化学状态 `C_t`、气象强迫 `M_t` 与地表排放 `E_t`：

```text
C_{t+1} = F_theta(C_t, M_t, E_t)
```

其中 `F_theta` 不是普通时空预测网络，而应逼近 WRF-Chem 所描述的状态演化。它至少必须同时通过：

1. **状态精度**：浓度、廓线、柱浓度与 teacher 一致；
2. **动力响应精度**：不同输送天气下 plume 演化合理；
3. **排放响应精度**：`dC/dE` 与 teacher 一致；
4. **滚动稳定性**：多小时 rollout 不出现发散或不物理漂移。

## 3. 核心逆问题

后验排放采用乘性校正：

```text
E_post = E_prior * exp(log_alpha)
```

通过固定或部分固定的前向算子得到三维 NO2，再经卫星观测算子 `H` 映射至 TROPOMI 原始 L2 像元：

```text
E_post → F_theta → C_3D → H → VCD_hat
                                   ↓
                             TROPOMI L2
```

优化对象是 `log_alpha`，而不是直接从零生成绝对排放。

## 4. 主尺度设计

### 全国主实验
- 中国大陆 + 区域输送缓冲；
- 参考水平尺度：12 km；
- neural vertical layers：6；
- 小时前向演化；
- 日尺度 TROPOMI 反演。

### 区域精细实验
- 华北平原；
- 长三角；
- 珠三角；
- 四川盆地；
- 参考尺度：3–6 km；
- neural vertical layers：8。

区域实验用于机制验证和尺度敏感性，不替代全国主结论。

## 5. 主研究期

参考设计：2021–2023。

但昂贵的 WRF-Chem teacher 不计划简单连续运行三年，而是围绕四季、典型污染过程、边界层状态和输送 regime 选择具有信息量的 episode，并设计排放干预 ensemble。

## 6. 五个项目产物

1. **Versioned teacher dataset**：带排放干预的 WRF-Chem 数据集；
2. **3D neural chemistry-transport operator**；
3. **Native-pixel satellite observation operator**；
4. **China-wide posterior NOx product**；
5. **2D-vs-3D inversion bias mechanism atlas / relationship**。

## 7. 什么才算项目成功

最低成功标准不是模型 MAE 比 baseline 小，而是：

- 前向状态 fidelity 通过；
- Jacobian/emission-sensitivity gate 通过；
- 后验排放在独立观测上优于 prior；
- 2D 与 3D 的差异可由边界层/输送物理解释；
- 该机制在多个气候/地形区域重复出现，或明确证明只在特定 regime 成立。

## 8. 明确不做的事

第一阶段不把以下内容强行塞入主模型：

- 全国 1–3 km 全年 WRF-Chem；
- 多污染物联合反演；
- 从零无先验绝对排放生成；
- 仅靠深度网络从 TROPOMI 直接回归排放；
- 用规则网格插值后的 Level-3 卫星图代替 L2 原始观测算子；
- 为追求模型复杂度而堆叠 Transformer/GNN 模块。
