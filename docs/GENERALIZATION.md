# 泛化与 OOD 实验设计

AtmosInv 不应只证明在同一全国网格、同一年度、随机切分数据上预测准确。真正有价值的问题是：模型是否学到可迁移的大气输送/排放响应规律。

## 1. 泛化维度

### Geographic OOD
采用 leave-one-region-out：
- YRD；
- NCP；
- PRD；
- SCB。

训练 teacher 可包含全国其他区域，但目标区域的 intervention episodes 从训练中完全移除。

### Meteorological OOD
保留未见：
- 极浅/极深 PBL；
- 强垂直风切变；
- frontal passage；
- persistent stagnation；
- coastal circulation；
- basin trapping。

### Emission OOD
测试：
- 未见缩放幅度；
- 未见空间 perturbation；
- 未见 sector perturbation；
- 未见 temporal pattern。

### Temporal OOD
训练 2021–2022，测试 2023，或反向设计；注意 teacher episode availability。

## 2. 泛化评价不只看 state RMSE

同时评价：
- forward state；
- vertical profile；
- TROPOMI-space column；
- Jacobian；
- inversion recovery；
- mechanism regime classification/relationship。

## 3. 迁移策略分级

1. zero-shot；
2. calibration-only；
3. small-sample fine-tuning；
4. full regional retraining。

高水平结论优先来自 1–2，而不是每个区域重新训练一套模型。

## 4. 防止“地理记忆”

加入以下诊断：
- 去掉 static location encoding；
- 经纬度随机/替换实验；
- 对比固定空间 embedding 与 physics features；
- source-map permutation sanity check。

如果模型严重依赖固定地理位置，需要重新解释其所谓 generalization。
