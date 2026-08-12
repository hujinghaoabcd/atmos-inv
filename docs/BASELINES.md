# Baseline 体系

## 1. Baseline 的目的

不是证明“我们的网络比老网络高几个点”，而是逐层回答复杂性是否必要。

## 2. Forward baselines

### B0 Persistence / climatological tendency
验证问题是否本身容易。

### B1 Regular-grid CNN/U-Net
证明图结构是否必要。

### B2 2D static GNN
只有水平空间传播。

### B3 2D wind-directed dynamic GNN
验证动态风图本身贡献。

### B4 3D static graph
验证显式垂直维度贡献。

### B5 3D physics dynamic graph
无 learned residual。

### B6 Full operator
physics graph + residual + chemistry + multiscale（最终配置以实验为准）。

## 3. Inversion baselines

至少准备：
- prior inventory/no inversion；
- simple column scaling；
- mass-balance/continuity inspired baseline；
- simplified 2D differentiable inversion；
- full 3D inversion。

若实现成熟传统 Bayesian/variational baseline 成本过高，可使用公开/可复现结果作为 context，但主比较中必须明确不可直接同条件比较的限制。

## 4. Fairness

所有 ML baselines 尽量统一：
- teacher split；
- forcing；
- optimization budget；
- input information；
- evaluation metrics。

不能让 proposed model 看到 3D WRF meteorology，而 baseline 只拿 10 m wind 后声称架构优势；信息优势和架构优势要拆开。

## 5. Baseline 输出

Main table 同时报告：
- state fidelity；
- rollout；
- column fidelity；
- Jacobian fidelity；
- inference cost。

避免单独以某一 RMSE 排名决定“最佳模型”。
