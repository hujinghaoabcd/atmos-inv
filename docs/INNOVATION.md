# 创新点与边界

## 1. 不应单独声称的创新

以下元素本身不足以构成本文核心 novelty：

- “首次把风场用于图邻接”；
- “动态有向 GNN”；
- “用深度学习替代 WRF-Chem”；
- “用 TROPOMI 反演 NOx”；
- “用 GraphCast 风格 encoder–processor–decoder”；
- “physics-informed GNN”；
- “全国尺度 AI 排放反演”。

这些方向均已有先行工作或明显邻近工作。本文创新必须来自**组合方式、逆问题设计和科学发现**。

## 2. 核心方法创新候选

### I1. 显式三维 atmospheric transport graph

节点为 `(x, y, z)` 大气单元，而不是把整个柱压成单个 2D 节点。水平边和垂直边分别表达：

- horizontal advection / dispersion；
- PBL mixing / vertical exchange。

### I2. Physics-initialized + learned residual connectivity

参考结构：

```text
A_t = A_physics(M_t) + DeltaA_theta(C_t, M_t)
```

物理图负责方向与可解释先验，可学习残差负责修正未解析输送。

### I3. Emission-intervention pretraining

teacher 数据不是只使用固定排放历史模拟，而是主动改变排放空间、部门、幅度和时间结构，让模型真正识别：

```text
dC / dE
```

这是模型能否用于 inverse problem 的基础。

### I4. Forward fidelity + sensitivity fidelity 双重验收

神经 surrogate 只有同时逼近：

```text
F(E, M)
```

和局部响应：

```text
J = dF/dE
```

才允许进入卫星反演。

### I5. Native-pixel differentiable observation operator

不将 TROPOMI 简单预插值为模型规则网格；将模型 3D state 投影到真实 L2 像元观测空间，并处理 vertical sensitivity / pressure mapping 等。

## 3. 最重要的科学创新候选

> 揭示传统 2D/近地输送卫星排放反演在特定边界层和垂直输送 regime 下产生系统性排放归因偏差，并确定该偏差的空间分布、条件和可迁移规律。

如果这一结果成立，模型只是发现机制的工具，论文上限显著高于单纯 neural surrogate。

## 4. 创新强度分层

### Level A — 工程/方法
神经 operator 显著加速 WRF-Chem forward response。

### Level B — 反演方法
神经 operator 能保持 emission sensitivity，并稳定用于卫星反演。

### Level C — 科学机制
发现 2D inversion bias 的系统性 atmospheric regime。

### Level D — 普适机制
该机制在多个气候、地形和排放区域可重复，能够形成统一或分 regime 的解释框架。

项目设计从一开始必须支持 A→D，而不是做完 A 后才临时想办法增加科学故事。
