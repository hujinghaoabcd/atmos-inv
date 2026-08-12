# AtmosInv 文档索引

本目录不是“最后补写的说明书”，而是项目的**研究设计源文件**。项目近期暂不启动，因此当前优先级是把未来容易遗忘、容易分叉、容易产生不可复现实验的决策提前写清楚。

## 1. 从哪里开始

建议按以下顺序阅读：

1. [`PROJECT_OVERVIEW.md`](PROJECT_OVERVIEW.md)：项目全景、研究边界和最终产物。
2. [`SCIENTIFIC_QUESTIONS.md`](SCIENTIFIC_QUESTIONS.md)：科学问题、假设与可证伪条件。
3. [`INNOVATION.md`](INNOVATION.md)：真正创新在哪里，哪些内容不能单独声称创新。
4. [`SYSTEM_ARCHITECTURE.md`](SYSTEM_ARCHITECTURE.md)：从卫星/气象/排放到反演的端到端结构。
5. [`DATA_CATALOG.md`](DATA_CATALOG.md) + [`DATA_DOWNLOAD_PLAN.md`](DATA_DOWNLOAD_PLAN.md)：数据清单与获取策略。
6. [`WRF_CHEM_PROTOCOL.md`](WRF_CHEM_PROTOCOL.md)：physics/chemistry teacher 设计。
7. [`TEACHER_DATASET_DESIGN.md`](TEACHER_DATASET_DESIGN.md)：排放干预样本与训练数据设计。
8. [`GRAPH_REPRESENTATION.md`](GRAPH_REPRESENTATION.md) + [`MODEL_DESIGN.md`](MODEL_DESIGN.md)：3D 图与神经算子。
9. [`ALGORITHM_IMPLEMENTATION_PLAN.md`](ALGORITHM_IMPLEMENTATION_PLAN.md)：代码模块、类接口、张量契约。
10. [`SATELLITE_OBSERVATION_OPERATOR.md`](SATELLITE_OBSERVATION_OPERATOR.md)：WRF/GNN 三维状态如何与 TROPOMI L2 比较。
11. [`INVERSION_PROTOCOL.md`](INVERSION_PROTOCOL.md)：NOx 后验排放反演。
12. [`JACOBIAN_VALIDATION.md`](JACOBIAN_VALIDATION.md)：能否用于反演的关键验收门。
13. [`EXPERIMENT_MATRIX.md`](EXPERIMENT_MATRIX.md)：正式实验编号与依赖关系。
14. [`VALIDATION_PLAN.md`](VALIDATION_PLAN.md)：独立验证与防止“自己验证自己”。
15. [`STARTUP_CHECKLIST.md`](STARTUP_CHECKLIST.md)：项目真正启动时逐项执行。

## 2. 文档分组

### 科学问题与创新
- `SCIENTIFIC_QUESTIONS.md`
- `INNOVATION.md`
- `MECHANISM_ANALYSIS.md`
- `LITERATURE_MAP.md`

### 数据与物理模式
- `DATA_CATALOG.md`
- `DATA_DOWNLOAD_PLAN.md`
- `DATA_SCHEMA.md`
- `DOMAIN_AND_SCALE.md`
- `WRF_CHEM_PROTOCOL.md`
- `TEACHER_DATASET_DESIGN.md`

### AI 与反演
- `GRAPH_REPRESENTATION.md`
- `MODEL_DESIGN.md`
- `ALGORITHM_IMPLEMENTATION_PLAN.md`
- `SATELLITE_OBSERVATION_OPERATOR.md`
- `INVERSION_PROTOCOL.md`
- `JACOBIAN_VALIDATION.md`

### 实验与评价
- `EXPERIMENT_MATRIX.md`
- `VALIDATION_PLAN.md`
- `GENERALIZATION.md`
- `ABLATION_SENSITIVITY.md`
- `MECHANISM_ANALYSIS.md`

### 工程、复现与管理
- `COMPUTE_STORAGE.md`
- `REPRODUCIBILITY.md`
- `RISK_REGISTER.md`
- `DECISIONS.md`
- `ROADMAP.md`
- `STATUS.md`
- `STARTUP_CHECKLIST.md`
- `HANDOFF_NEXT_CONVERSATION.md`

### 论文
- `PAPER_PLAN.md`
- `PAPER_EVIDENCE_MAP.md`

## 3. 文档状态约定

每项设计可处于：

- **FROZEN**：除非有新证据，不随意改变；改变必须记录 ADR。
- **REFERENCE DEFAULT**：当前推荐默认值，可在 benchmark 后调整。
- **OPEN**：尚未决定，禁止在正式实验中静默自行选择。
- **DEPRECATED**：曾经考虑，但已明确不再使用。

任何会改变论文科学解释的设置，都必须进入 `DECISIONS.md`。
