# 下一次接手 / 对话交接

## 项目一句话

AtmosInv 计划利用 WRF-Chem emission-intervention teacher 训练一个保持排放敏感度的 3D graph neural chemistry–transport operator，再通过 native-pixel TROPOMI observation operator 反演全国日尺度 NOx correction，并研究 2D inversion 在哪些 atmospheric regimes 下产生系统性排放归因偏差。

## 当前阶段

M0，设计完成但科学实验尚未启动。

## 不要重新讨论已确定原则

除非出现新证据，否则保留：
1. 全国主实验 + 区域 refinement；
2. WRF-Chem teacher；
3. emission intervention；
4. 3D explicit transport；
5. native L2 satellite comparison；
6. multiplicative prior correction；
7. Jacobian gate；
8. 独立 validation；
9. 论文重点最终应落在 2D-vs-3D mechanism，而不是模型换代。

## 第一次重新启动时做什么

1. 阅读 `STATUS.md`；
2. 阅读 `DECISIONS.md`；
3. 更新近期文献 `LITERATURE_MAP.md`；
4. 按 `STARTUP_CHECKLIST.md` Phase 0 做版本核验；
5. 只下载 TROPOMI/ERA5 小样本；
6. 冻结 WRF-Chem chemistry pathway；
7. 做 24 h benchmark；
8. 更新真实存储/工时估算。

## 最危险的遗忘点

- forward RMSE 好 ≠ inversion 可用；必须验证 `dC/dE`；
- TROPOMI 是 retrieval observation，不是规则网格 ground truth；
- 固定历史 emission teacher 可能让网络忽略 emission input；
- WRF-Chem 输出不可无限保存；
- CNEMC 默认不进入主反演 loss；
- 2D vs 3D 的差异需要机制解释和跨区域检验。
