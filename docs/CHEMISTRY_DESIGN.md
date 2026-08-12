# 化学表示与 WRF-Chem 机制选择

## 1. 为什么现在不冻结 `chem_opt`

`chem_opt` 会同时决定：
- 可用 species；
- emission speciation；
- chemical IC/BC mapping；
- computational cost；
- teacher chemistry bias；
- neural state dimension。

因此不能先下载一套 chemical BC 后再倒推 mechanism。

## 2. 最低 neural chemistry state

首选核心 family：

```text
NO, NO2, O3
```

原因：NO2 柱与 NOx emission 的联系不能完全忽略 NO–NO2–O3 快速循环。

## 3. 扩展候选

- HNO3；
- PAN；
- HCHO；
- CO；
- selected VOC lumped species。

扩展条件：它们能明显改善 NO2 evolution / sensitivity，而不是因为 WRF-Chem 输出中“有这个变量”。

## 4. Chemistry operator 三种路线

### C1 Black-box local MLP
最容易实现，作为 baseline。

### C2 Residual chemistry
以简化解析/数值 chemistry tendency 为基准，网络学 residual。

### C3 Neural ODE / gated tendency
更适合反应时间尺度，但复杂度更高。

先从 C1/C2 benchmark，不预设 Neural ODE 一定更好。

## 5. 化学与 transport 解耦测试

用 controlled teacher samples：
- weak transport / strong chemistry；
- strong transport / similar radiation；
- day/night transition。

检查模型是否把 transport error 错当 chemistry correction。

## 6. 质量守恒与 family diagnostics

根据选择的 species representation，定义可解释的 family tendency diagnostic，而不是随意要求所有物种单独守恒。

## 7. Freeze criteria

正式 `chem_opt` 选择应记录：
- literature rationale；
- China 12 km feasibility；
- NO2/O3 validation；
- emission/BC availability；
- runtime/storage；
- species mapping audit。
