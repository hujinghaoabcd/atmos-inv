# NOx 排放反演协议

## 1. 参数化

主方案：

```text
E_post(i,t) = E_prior(i,t) * exp(log_alpha(i,t))
```

优点：
- 后验非负；
- 以 prior 为中心；
- correction factor 可解释；
- 可控制正则化强度。

第一阶段不从零直接生成绝对 emission field。

## 2. 反演时间尺度

TROPOMI 主方案：daily correction。小时级 forward operator 负责当天大气输送，但优化参数无需每小时完全自由，否则可识别性不足。

候选参数化：
- daily scalar per cell；
- daily low-rank spatial basis；
- daily × sector correction；
- smooth temporal latent process。

## 3. Objective

参考结构：

```text
L = L_satellite
  + λ_prior L_prior
  + λ_space L_space
  + λ_time L_time
  + λ_phys L_physics
```

其中地面观测默认作为独立 validation，避免既用于反演又用于评价造成乐观偏差。

## 4. Prior regularization

候选：
- Gaussian on `log_alpha`；
- spatially varying prior uncertainty；
- sector-dependent uncertainty。

不能默认所有格点清单不确定性相同。

## 5. Spatial regularization

必须谨慎。太强会把真实局地源抹平；太弱会出现 pixel-level compensation noise。比较：
- graph Laplacian；
- total variation；
- multiscale latent correction。

## 6. Identifiability

核心风险：不同 emission patterns + chemistry/transport error 可能产生相似 column。需要：
- prior；
- multi-day dynamics；
- intervention-trained sensitivity；
- independent validation；
- uncertainty analysis。

## 7. Optimization

第一阶段候选：gradient-based deterministic optimization。只有稳定后再考虑：
- ensemble posterior；
- variational uncertainty；
- amortized inverse network。

不要先训练一个 `TROPOMI → emission` encoder 直接给出后验而跳过 forward closure。

## 8. Twin experiments

真实卫星反演前必须进行：
1. 从已知 emission perturbation 生成 teacher/synthetic observation；
2. 只给模型 observation + prior；
3. 检查是否恢复已知 correction；
4. 分析 spatial leakage 与 magnitude bias。

这是反演代码正确性的硬门槛。

## 9. Posterior 验收

不能只报告 satellite loss 下降。至少报告：
- correction magnitude distribution；
- spatial smoothness / artifact；
- independent forward validation；
- ground NO2/O3 change；
- regional/sector plausibility；
- sensitivity to prior strength；
- sensitivity to QA and observation errors。
