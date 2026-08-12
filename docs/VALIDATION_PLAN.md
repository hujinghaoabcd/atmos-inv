# 验证体系

## 1. 四层验证

### Layer A — WRF-Chem teacher quality
验证 teacher 是否足够可信。

### Layer B — Neural forward fidelity
验证 `C_hat` 与 teacher 的 state/profile/column 一致性。

### Layer C — Sensitivity fidelity
验证 `dC/dE`。

### Layer D — Real-world posterior validation
验证反演后的 emissions 是否改善独立真实观测。

任何一层失败都不能用下一层“结果看起来不错”掩盖。

## 2. Teacher validation

气象：
- wind；
- temperature；
- PBLH（若有可比数据/再分析）；
- precipitation/cloud context。

化学：
- surface NO2/O3；
- satellite NO2 column；
- optional column/profile sites。

## 3. Neural forward metrics

不要只用 global RMSE：
- MAE/RMSE/bias；
- spatial correlation；
- temporal correlation；
- vertical profile error；
- column error；
- high-emission vs background；
- seasonal/regime stratification；
- rollout drift。

## 4. Posterior validation

### 默认 out-of-loop
CNEMC surface NO2/O3 不进入主 satellite loss，而用于验证。

### 更强证据
- Pandora/MAX-DOAS；
- CEMS；
- power/traffic/activity changes；
- independent CTM rerun with posterior emissions。

## 5. Avoid circular validation

禁止：
- 用同一 TROPOMI 像元优化后，再把同一像元 residual 当成“独立验证”；
- 用 teacher 模型产生 synthetic target，再把 teacher agreement 宣称为真实排放准确；
- 用 MEIC 当 prior，又以接近 MEIC 作为 posterior 正确证据。

## 6. Stratified validation

结果至少按：
- season；
- PBL regime；
- wind regime；
- emission intensity；
- region；
- urban/rural；
- terrain/coast/basin；
- cloud/QA category
分层检查。

## 7. 统计不确定性

最终比较不仅报告单次指标。需要：
- multiple seeds for neural model；
- bootstrap over days/episodes；
- confidence intervals；
- paired significance/effect size where appropriate；
- spatial autocorrelation-aware interpretation。
