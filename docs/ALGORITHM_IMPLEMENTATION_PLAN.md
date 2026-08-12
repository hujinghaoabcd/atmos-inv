# 算法实现规格与代码计划

本文件定义未来代码如何落地。任何实现 PR 应先找到对应接口，而不是在 notebook 中形成第二套逻辑。

## 1. 目标包结构

```text
src/atmos_inv/
├── data/
│   ├── manifest.py
│   ├── tropomi.py
│   ├── era5.py
│   ├── emissions.py
│   └── teacher.py
├── wrfchem/
│   ├── run_manifest.py
│   ├── namelist.py
│   ├── extract.py
│   └── vertical.py
├── graph/
│   ├── schema.py
│   ├── grid.py
│   ├── horizontal.py
│   ├── vertical.py
│   └── multiscale.py
├── models/
│   ├── transport.py
│   ├── chemistry.py
│   ├── operator.py
│   └── baselines/
├── satellite/
│   ├── tropomi_product.py
│   ├── overlap.py
│   ├── vertical_mapping.py
│   └── observation.py
├── inversion/
│   ├── parameterization.py
│   ├── objective.py
│   ├── regularization.py
│   └── solve.py
└── evaluation/
    ├── forward.py
    ├── jacobian.py
    ├── inversion.py
    ├── generalization.py
    └── mechanism.py
```

## 2. 张量契约

推荐训练 batch：

```text
state:      [B, Z, N, C_state]
met_3d:     [B, Z, N, C_met]
met_2d:     [B, N, C_met2d]
emission:   [B, N, C_emit]
edge_index: [2, E] or hierarchical edge collections
edge_attr:  [B, E, C_edge]  # dynamic meteorological edges
```

对于规则 grid，也允许 `[B, Z, Y, X, C]` 存储，进入 graph processor 前再 flatten。数据存储格式与模型运行格式不要强绑定。

## 3. 主要类接口

### `TeacherSample`
返回一个 transition：`t → t+1`，同时携带 provenance key。

### `GraphBuilder`

```python
build(static_grid, met_t) -> GraphBatch
```

### `TransportOperator`

```python
forward(state, forcing, graph) -> transported_state_or_tendency
```

### `ChemistryOperator`

```python
forward(transported_state, local_met) -> next_state_or_tendency
```

### `AtmosphericOperator`
组合 transport + chemistry，并提供 rollout：

```python
rollout(initial_state, meteorology_seq, emission_seq, steps)
```

### `SatelliteObservationOperator`

```python
project(model_state_3d, satellite_batch) -> predicted_observations
```

必须是 batchable，并尽可能保持 autograd path。

### `EmissionParameterization`

```python
posterior(prior, latent_correction) -> E_post
```

## 4. 实现阶段

### A0 — synthetic
4×4×3 toy atmosphere，确认形状、方向边、垂直边和梯度。

### A1 — teacher slice
单个真实 WRF-Chem 小切片，确认读取、单位、垂直映射。

### A2 — 1-step operator
只训练 `t→t+1`。

### A3 — rollout
6/12/24 h curriculum。

### A4 — emission intervention
引入 sensitivity loss/evaluation。

### A5 — satellite projection
接 L2 small sample。

### A6 — inversion toy recovery
先在 synthetic/teacher truth 上反演已知 emission perturbation。

### A7 — real TROPOMI inversion
只有前六关通过后启动。

## 5. 单元测试重点

- unit conversion；
- grid flatten/unflatten；
- edge direction；
- vertical mapping conserves column/mass within tolerance；
- observation overlap weights sum correctly；
- log emission correction positivity；
- masked satellite loss；
- gradient reaches `log_alpha`；
- checkpoint/resume determinism within expected tolerance。

## 6. 性能策略

- sparse graph operations；
- AMP；
- gradient checkpointing；
- patch/mesh batching；
- lazy xarray/zarr reads；
- precomputed static topology；
- dynamic edge features on demand；
- distributed data parallel only after single-node correctness。

## 7. 禁止 premature optimization

不要在 observation operator、单位转换、vertical mapping 尚未通过数值验证前做 CUDA 自定义核或复杂分布式优化。科学正确性先于吞吐率。
