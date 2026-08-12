# Neural Teacher 与反演数据 Schema

本文件定义未来处理后数据的逻辑结构。实际 chunk 大小必须通过 I/O benchmark 冻结。

## 1. Teacher dataset 逻辑维度

推荐统一：

```text
sample / episode
time
level
y
x
species
feature
```

核心数组：

```text
state_chem[time, level, y, x, species]
met_3d[time, level, y, x, met_feature]
met_2d[time, y, x, met2d_feature]
emission[time, y, x, sector_or_species]
```

以及：

```text
cell_area[y, x]
terrain[y, x]
lat[y, x]
lon[y, x]
vertical_bounds[time, level, y, x]  # 若采用动态物理层映射
```

## 2. 样本必须带 provenance

每个 episode/sample 可回溯：

- teacher_dataset_version；
- wrf_run_id；
- intervention_id；
- emission_parent_manifest；
- meteorology_parent_manifest；
- chem_icbc_manifest；
- WRF-Chem config hash；
- processing code Git SHA。

## 3. Vertical aggregation

原始 WRF-Chem native levels 不直接丢弃。生成两层产品：

```text
teacher/native_selected/
teacher/neural_6layer/
```

这样未来如果 6 层设计有问题，可以重新聚合而不用重跑 WRF-Chem。

## 4. 图数据不建议永久复制全部 edge list

对于规则 WRF 网格：
- static topology 可只保存索引模板；
- dynamic edge features 由气象场在线/缓存生成；
- multiscale mapping 单独版本化保存。

否则动态边会造成巨大重复存储。

## 5. Satellite match table

建议建立 observation table：

```text
obs_id
orbit_id
time
pixel_polygon
vcd
uncertainty
qa
cloud
amf
ak_ref
model_overlap_indices
model_overlap_weights
```

大数组如 AK 可放 array store，表里保存 key/index。

## 6. 数值精度

- raw scientific products：保持原始 dtype；
- processed teacher：默认 float32；
- training batch：允许 mixed precision；
- emission totals / conservation diagnostics：必要时 float64 计算。

## 7. Split metadata

train/val/test split 不能只存在 Python seed 中，必须落盘为版本化 split manifest，按 episode/region/intervention 分组。
