# AtmosInv

**面向全国尺度卫星约束 NOx 排放反演的三维图神经大气算子研究框架**

当前状态：**M0 — 设计与准备阶段，正式科学实验尚未启动。**

AtmosInv 的核心不是“再做一个空气质量 GNN”，而是回答：

> 当卫星观测的是整层 NO2 柱时，如果反演模型没有显式表示垂直混合和三维区域输送，会不会把输送来的 NO2 错误归因到本地地表排放？这种偏差在什么边界层、风切变、地形和输送条件下发生？

计划路线：

```text
ERA5 + emissions + chemical IC/BC
            ↓
         WRF-Chem
            ↓
 emission-intervention teacher
            ↓
3D graph neural chemistry-transport operator
            ↓
       3D NO2 state
            ↓
TROPOMI native-pixel observation operator
            ↓
 differentiable NOx inversion
            ↓
     posterior emissions
            ↓
2D vs 3D atmospheric mechanism analysis
```

全国参考尺度为 12 km，并设计华北平原、长三角、珠三角、四川盆地 3–6 km refinement。主卫星为 TROPOMI L2 NO2，参考时段为 2021–2023。

一个模型只有同时满足：

```text
C_neural ≈ C_WRF-Chem
```

以及：

```text
dC_neural/dE ≈ dC_WRF-Chem/dE
```

才允许进入真实卫星反演。

完整研究设计见 [`docs/README.md`](docs/README.md)。
