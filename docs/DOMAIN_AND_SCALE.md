# 空间、垂直与时间尺度设计

## 1. 全国主尺度

参考默认：12 km。原因不是认为 12 km 是“最佳物理分辨率”，而是它在全国尺度上可以同时支持：
- mesoscale transport；
- 城市群尺度排放结构；
- 多尺度图；
- 与几公里级卫星像元的合理 observation mapping。

最终 WRF domain 的投影、`e_we/e_sn`、中心点、true latitudes 必须在实际 benchmark 时冻结。

## 2. 区域尺度

3–6 km 区域嵌套用于：
- 检查全国结论是否受粗网格影响；
- 复杂地形；
- 城市群 plume；
- satellite pixel / grid mismatch sensitivity。

区域 refinement 不是单独换一套完全不同的模型；优先复用 national operator representation 或 fine-tune。

## 3. 垂直尺度

WRF-Chem teacher 保留 native vertical structure；神经模型初始使用 6 层，全国与区域可扩到 8 层。

候选物理层：
1. near-surface；
2. lower PBL；
3. mid PBL；
4. upper PBL；
5. lower free troposphere；
6. upper transport layer。

注意：PBLH 随时空变化。固定 pressure bin 与 PBL-relative bin 都要作为候选方案比较，不能先假设动态 PBL-relative 一定更好。

## 4. 时间尺度

- WRF-Chem output：1 h；
- neural operator：1 h transition；
- rollout：从 1 h 逐步验证到 6/12/24 h；
- TROPOMI inversion：daily emission correction；
- GEMS extension：daytime sub-daily/hourly。

## 5. 卫星与模型尺度不一致

不强迫 TROPOMI 重采样到 12 km。模型状态通过 observation operator 与真实像元 footprint 比较，因此 observation scale 与 model scale 保持独立。

## 6. 多尺度图

全国参考：

```text
12 km ↔ 36 km ↔ 108 km
```

功能：
- fine：局地 plume；
- middle：城市群/区域输送；
- coarse：长距离信息传播。

尺度组合必须通过 ablation 验证，不因“像 GraphCast”而默认正确。
