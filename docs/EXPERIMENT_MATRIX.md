# 正式实验矩阵

所有论文实验必须使用稳定 Experiment ID。

## E0xx — 数据/基础设施

### E000 Repository bootstrap
当前阶段，仅验证结构、配置和文档。

### E010 Data product audit
核对产品版本、变量、时间、checksum、单位。

### E020 Observation-operator unit benchmark
TROPOMI small-orbit mapping 验证。

## E1xx — WRF-Chem / Teacher

### E100 Baseline WRF-Chem
冻结 physics/chemistry/domain。

### E110 Meteorological regime catalog
为 seasonal episodes 建标签。

### E120 Emission-intervention ensemble
形成 `dC/dE` 信息。

### E130 Teacher dataset release
发布 immutable teacher version + split。

## E2xx — Forward Operator

### E200 Simple grid baselines
CNN/U-Net 等。

### E210 2D GNN
不显式垂直输送。

### E220 Static 3D graph
只测试 3D representation 本身。

### E230 Dynamic physics graph
风/PBL 驱动。

### E240 Full graph neural chemistry-transport operator
主模型。

### E250 Rollout stability
1/6/12/24 h。

## E3xx — Sensitivity

### E300 Neural finite-difference sanity
### E310 Autograd vs neural finite difference
### E320 Neural vs WRF-Chem Jacobian
### E330 Unseen intervention sensitivity

E320/E330 是进入真实 inversion 的 gate。

## E4xx — Inversion

### E400 Synthetic twin inversion
### E410 Teacher-truth perturbation recovery
### E420 TROPOMI daily inversion
### E430 Prior-strength sensitivity
### E440 Observation QA sensitivity
### E450 Optional GEMS sub-daily experiment

## E5xx — Science mechanism

### E500 2D vs 3D posterior difference
### E510 Boundary-layer regime analysis
### E520 Vertical shear / transport analysis
### E530 Terrain/coastal/basin stratification
### E540 Cross-region mechanism synthesis

## E6xx — Generalization

### E600 Leave-YRD-out
### E610 Leave-NCP-out
### E620 Leave-PRD-out
### E630 Leave-SCB-out
### E640 Unseen year
### E650 Unseen meteorological extremes

## E7xx — Ablation / sensitivity

- vertical layers；
- graph hierarchy；
- learned residual edges；
- chemistry operator；
- intervention sampling；
- satellite observation operator simplification；
- regularization。

## E8xx — Regional refinement

3–6 km focused experiments，验证全国尺度 conclusions。

## E9xx — Paper reproduction

### E900 Main table reproduction
### E910 Main figure reproduction
### E920 Supplement reproduction
### E990 Final archival run

论文提交前必须执行 E9xx，而不能直接用开发期零散 run 拼表。
