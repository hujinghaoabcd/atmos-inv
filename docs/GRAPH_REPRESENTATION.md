# 三维大气图表示

## 1. 节点

节点代表模型网格中的 `(i, j, k)` 大气单元。节点特征候选：

```text
chemical state: NO, NO2, O3, ...
meteorology: U, V, W, T, RH/Q, pressure
boundary layer: PBLH-relative position, mixing proxy
static: terrain, land/sea, cell area
forcing: surface emission injection (bottom layers)
```

## 2. 水平边

不是单纯距离 kNN。参考 physics edge feature：

```text
distance
relative bearing
u · r_hat
v · r_hat
wind speed
stability / PBL context
terrain difference
```

方向性要求：`A_ij != A_ji`。

## 3. 垂直边

连接同一水平单元的相邻/跨层节点：

```text
vertical distance
W / omega proxy
PBLH relation
mixing coefficient/proxy
stability
layer thickness
```

是否允许非相邻跨层 shortcut 必须由 sensitivity experiment 决定。

## 4. Physics-initialized + residual graph

设计候选：

```text
edge_weight = physical_gate * learned_gate
```

或：

```text
edge_logit = physical_logit + learned_residual
```

优先选择不容易产生负传输和数值爆炸的参数化。

## 5. 多尺度图

全国参考：12/36/108 km。实现方式候选：
- hierarchy pooling；
- mesh nodes；
- parent-child bipartite edges；
- encoder → multiscale processor → decoder。

## 6. 图不是流体方程的替代定义

图结构只是表示 transport connectivity。真正的物理约束还需要：
- state update form；
- conservation diagnostics；
- positivity；
- boundary handling；
- source injection；
- chemistry coupling。

## 7. 必须记录的 ablation

- distance graph；
- static geographic graph；
- dynamic wind graph；
- + vertical graph；
- + physics edge features；
- + learned residual；
- + multiscale。

目的不是证明每一步都提高 RMSE，而是确定哪个结构真正改善 `dC/dE` 和 2D/3D mechanism fidelity。
