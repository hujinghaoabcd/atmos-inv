# 3D Neural Chemistry–Transport Operator 设计

## 1. 目标

学习：

```text
(C_t, M_t, E_t) → C_{t+1}
```

而不是：

```text
meteorology → next NO2 map
```

模型必须显式接收排放 forcing，并在 intervention test 上体现正确响应。

## 2. 推荐结构：operator splitting

```text
C_t
 ├─ emission injection
 ↓
Transport Operator (GNN)
 ↓
C_transport
 ↓
Local Chemistry Operator (MLP / gated ODE-like block)
 ↓
C_{t+1}
```

### Transport block
负责 spatial message passing：水平平流、区域输送、垂直交换。

### Chemistry block
对每个大气单元执行共享的局地映射，条件包括 T、RH、radiation 等。

这种分解优于让单个 black-box GNN 同时承担空间输送与局地反应。

## 3. 状态物种

最低核心：
- NO；
- NO2；
- O3。

扩展候选：HNO3、PAN、HCHO、CO。扩展必须由 teacher chemistry 和性能收益支持。

## 4. 输入 forcing

- meteorology 3D；
- PBLH / radiation；
- surface/sector emissions；
- boundary context；
- optional previous tendencies。

## 5. 输出策略

候选：
1. 直接预测 `C_{t+1}`；
2. 预测 tendency `Delta C`；
3. 预测 log/positive transformed state；
4. residual over simplified physics tendency。

优先 benchmark tendency/residual，因为更接近状态演化且可能提高 rollout 稳定性。

## 6. 约束

至少监控：
- positivity；
- mass tendency consistency；
- emission-response monotonicity（仅在适用 regime）；
- numerical stability；
- boundary flux；
- NOx family consistency（根据 chemistry representation）。

## 7. Loss families

前向训练候选：

```text
L = L_state
  + λ_profile L_profile
  + λ_column L_column
  + λ_tendency L_tendency
  + λ_cons L_conservation
  + λ_roll L_rollout
```

不要把所有项第一天全部打开。先单步状态 → rollout → sensitivity 分阶段增加。

## 8. Baselines

必须至少包括：
- persistence / simple tendency；
- CNN/U-Net 类规则网格模型；
- 2D GNN；
- static 3D graph；
- dynamic 3D graph；
- 简化 physical transport baseline；
- full proposed operator。

## 9. 不以参数量作为贡献

项目不追求训练一个 10^9 参数“大气大模型”。借鉴 weather foundation models 的是：
- state evolution operator；
- multiscale representation；
- heterogeneous forcing；
- pretrain → inverse downstream task；
- physics/learned hybridization。
