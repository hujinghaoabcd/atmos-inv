# 垂直层压缩与映射设计

## 1. 目标

WRF-Chem 可以保留 35–45+ native layers，但 neural operator 不一定需要逐层图节点。压缩目标是保留对 NOx transport/inversion 有意义的垂直结构，同时减少图规模。

## 2. 候选方案

### V1 Fixed pressure/height bins
优点：稳定、易比较；缺点：不能随 PBL 变化。

### V2 PBL-relative layers
例如 surface/lower/mid/upper PBL + free troposphere。

优点：物理意义强；缺点：PBLH 突变时层边界动态，可能引入 numerical discontinuity。

### V3 Hybrid
近地/PBL relative + free-tropospheric fixed pressure bins。

## 3. 聚合量守恒

浓度/mixing ratio 不能简单算术平均。根据状态变量定义采用：
- air-mass weighted；
- pressure thickness weighted；
- partial-column conserving aggregation。

具体公式需根据 WRF 输出变量单位写测试。

## 4. 必须通过的测试

- 聚合前后 tropospheric column tolerance；
- known uniform-profile analytical test；
- sharp PBL profile test；
- PBLH crossing test；
- satellite observation operator consistency。

## 5. 层数消融

1/3/6/8 layers。主结论若只在 8 层出现而 6 层完全消失，需要解释是物理信息还是模型容量。

## 6. 存储

长期保存 selected native layers/variables，使 vertical scheme 可重新计算；不要只保存一次 6-layer product 后删掉所有可重构信息。
