# Emission-Intervention Teacher Dataset 设计

## 1. 为什么固定历史排放训练不够

如果所有训练样本的排放空间结构几乎固定，网络可以通过 `C_t + meteorology` 获得很低的预测误差，却忽略 emission input。这样的模型即使浓度 RMSE 很好，也可能有错误的 `dC/dE`，不能用于 inversion。

因此 teacher 必须包含**主动排放干预**。

## 2. 干预类型

### A. 全域幅度缩放
参考候选：0.5 / 0.75 / 1.25 / 1.5。

用途：检查整体 sensitivity、非线性和 saturation。

### B. 空间块/区域扰动
对部分城市群、随机连续区域、上风向源区进行增减。

必须使用 spatially coherent perturbation，避免只做像素独立白噪声。

### C. 部门扰动
交通、电力、工业等单独变化，用于判断是否可识别 sector-specific response。

### D. 时间扰动
改变 diurnal profile、weekday/weekend 或短时 episode，测试 response timing。

## 3. Experimental design

不一定穷举所有组合。可采用：
- space-filling design；
- Latin hypercube；
- structured factorial subset；
- active-learning selection。

正式方法在 pilot sensitivity 后冻结。

## 4. 关键原则：扰动必须可识别

如果两个 intervention 产生几乎相同的大气响应，就没有必要重复投入昂贵 WRF-Chem 成本。先用小域/短期 benchmark 估计 intervention information gain。

## 5. Split 防泄漏

禁止随机切小时。

至少设置：
- unseen episode；
- unseen meteorological regime；
- unseen perturbation pattern；
- unseen region；
- optional unseen year。

## 6. Teacher version

```text
teacher_vMAJOR.MINOR.PATCH
```

- MAJOR：WRF-Chem/chemistry/domain/split 改变；
- MINOR：加入新 episode/intervention；
- PATCH：metadata/processing bug，不改变科学内容。

## 7. Teacher sampling unit

候选两种：
- full-domain time step；
- spatiotemporal patch。

全国模型优先考虑 patch/mesh batching，但必须保持跨 patch transport 边界信息；不能因训练方便切断大尺度输送。

## 8. Normalization

气象、浓度、排放使用训练集统计量。对 heavy-tailed emissions 可比较 log transform / robust scaling。所有 scaler 必须版本化并只从 train split 计算。

## 9. Acceptance gate

teacher dataset 发布前必须回答：
- 干预是否覆盖足够 emission amplitude？
- 是否覆盖 major meteorological regimes？
- test 中是否真正包含未见 perturbation？
- 每个样本是否可追到 WRF run？
- 是否存在 data leakage？
