# 端到端系统架构

## 1. 总体数据流

```text
TROPOMI L2 ───────────────────────────────────────────────┐
                                                         │
ERA5 → WPS/WRF → WRF meteorology                         │
                  │                                      │
MEIC/CAMS → WRF-Chem emissions                           │
                  │                                      │
Chemical IC/BC ───┼→ WRF-Chem teacher simulations       │
                  │             │                        │
                  │             ├→ baseline              │
                  │             └→ emission interventions│
                  │                       │               │
                  │                  teacher dataset      │
                  │                       │               │
                  └────────────→ 3D neural operator      │
                                          │               │
                                  3D chemical state       │
                                          │               │
                               satellite observation H ───┘
                                          │
                                  satellite-space loss
                                          │
                                optimize emission factor
                                          │
                                   posterior NOx
```

## 2. 模块边界

### Data layer
职责：获取、版本、校验、裁剪、坐标/时间标准化。禁止夹带模型逻辑。

### WRF-Chem layer
职责：生成物理 teacher 和排放干预响应。禁止将 WRF-Chem 输出直接视为“真值排放”。

### Teacher layer
职责：将巨大的 native output 转换为版本化 neural dataset；记录从每个样本回溯到 WRF run 的关系。

### Graph layer
职责：把网格、垂直层、气象输送信息转为图结构和 edge features。

### Neural operator layer
职责：逼近状态演化算子，不读取 TROPOMI 标签完成 teacher pretraining。

### Satellite layer
职责：把三维状态转换到真实观测空间；产品版本变化只应局部影响该层。

### Inversion layer
职责：优化 emission correction，不重复实现 forward physics。

### Evaluation layer
职责：前向、Jacobian、反演、泛化、机制分析相互独立。

## 3. 两阶段训练/反演

### Stage A — Forward operator learning

```text
(C_t, M_t, E_t) → F_theta → C_{t+1}
```

监督来自 teacher。

### Stage B — Satellite-constrained inversion

冻结或严格控制 `F_theta`：

```text
log_alpha → E_post → rollout(F_theta) → H → y_hat
```

与 TROPOMI `y_obs` 比较并反向传播至 `log_alpha`。

## 4. 关键隔离

- CNEMC 默认用于独立 validation，不用于主 inversion loss；
- TROPOMI 训练/优化像元与独立卫星验证集合需分开；
- teacher train/val/test 按 episode/region/perturbation 分组，不能随机打散相邻小时导致泄漏；
- 任何 satellite preprocessing 的改变不得静默改变 teacher dataset version。

## 5. 未来扩展接口

架构预留但第一阶段不实现：
- GEMS hourly observation operator；
- HCHO/VOC 联合反演；
- aerosol/PM；
- probabilistic operator / ensemble uncertainty；
- regional fine-tuning；
- global transfer。
