# 风险登记与替代路线

## R1. WRF-Chem 全国模拟成本过高
**影响：高**

缓解：episode sampling、intervention information gain、区域高分/全国中分辨率、减少永久输出。

Fallback：先完成全国 12 km limited episodes + 区域干预，而不是全年全国 ensemble。

## R2. Neural operator forward 好但 Jacobian 差
**影响：致命于反演**

缓解：emission-intervention training、sensitivity loss、architecture/forcing audit。

Fallback：神经 operator 仅作为 forward emulator，不直接反演；用 conventional inversion 或 hybrid gradient approximation。

## R3. WRF-Chem chemistry bias 被网络复制

缓解：真实 TROPOMI/ground out-of-loop validation；satellite fine adjustment；多机制 sensitivity。

Fallback：研究 transport sensitivity 而弱化 absolute chemistry claim。

## R4. 2D vs 3D 差异不显著

这不是项目失败。可能说明大多数 TROPOMI-scale daily inversion 中 2D approximation 足够。

转化为科学结论：确定 3D 必要性的边界条件，并量化哪些 regime 不需要复杂 3D 模型。

## R5. 后验排放不可识别

缓解：stronger prior、lower-dimensional correction、multi-day dynamics、sector aggregation、GEMS/ground auxiliary evidence。

Fallback：反演 regional scaling 而非 grid-cell daily correction。

## R6. TROPOMI observation operator 实现误差

缓解：small-orbit analytical tests、官方产品文档、独立 comparison workflow、版本锁定。

这是高优先级 correctness risk。

## R7. 数据产品版本在三年内变化

缓解：manifest processor version；分版本处理；重处理一致版本优先。

## R8. 地面站历史数据不完整/元数据缺失

Fallback：以 satellite holdout + available column sites + independent CTM 为主，明确验证范围。

## R9. 多尺度 GNN 太复杂

Fallback：先使用单尺度 12 km physics graph。多尺度是增强项，不应成为项目启动依赖。

## R10. 项目停顿造成上下文丢失

缓解：`STATUS.md`、`DECISIONS.md`、`HANDOFF_NEXT_CONVERSATION.md`、Experiment IDs 和 manifests 持续维护。
