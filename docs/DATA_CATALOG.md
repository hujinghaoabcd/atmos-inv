# 数据目录与版本契约

> 本文件记录“需要什么数据以及为什么”。具体下载命令、API 和批处理策略见 `DATA_DOWNLOAD_PLAN.md`。

## 1. 统一研究时段

参考主时段：**2021-01-01 至 2023-12-31**。

昂贵 teacher 模拟只选择代表性 episode；卫星和地面观测尽可能保留三年全量以支持反演、泛化和独立验证。

## 2. 数据表

| ID | 数据 | 推荐产品/版本策略 | 时间 | 用途 | 长期保存 |
|---|---|---|---|---|---|
| SAT-TROP-NO2 | Sentinel-5P/TROPOMI NO2 | L2 OFFL/RPRO，记录 processor version | 2021–2023 | 主卫星约束 | 原始 L2 必存 |
| SAT-GEMS-NO2 | GEMS NO2 | L2，记录算法版本 | 2021–2023 | 小时验证/扩展 | 可选全量 |
| MET-ERA5 | ERA5 | pressure/model-level + single-level 按 WRF workflow | teacher episodes；必要时三年 | WRF 气象 IC/BC | 原始驱动必存 |
| EMI-MEIC | MEIC | 2020 prior，保留 sector/species | 基准年 | 中国人为排放 prior | 必存 |
| EMI-GLOBAL | CAMS-GLOB-ANT 或冻结的全球清单 | 与研究期匹配 | 2021–2023/基准 | 域外人为排放 | 必存 |
| CHEM-BC | CAM-chem/WACCM 或经验证的 CAMS 路线 | 与 chem_opt 一起冻结 | teacher episodes | chemical IC/BC | 必存 |
| STATIC-WPS | WPS geographic static data | 冻结包版本 | 静态 | geogrid | 必存 |
| OBS-CNEMC | 全国地面空气质量站 | hourly NO2/O3 + metadata | 2021–2023 | 独立验证 | 必存 |
| OBS-COLUMN | Pandora/MAX-DOAS | 站点可用期 | 可选 | column/profile validation | 可选 |
| AUX-CEMS | CEMS/活动数据 | 仅可靠来源 | 可用期 | 排放独立证据 | 可选 |

## 3. TROPOMI 必保留内容

至少要保留原始文件中与以下概念有关的变量，而不是只导出 VCD：

- tropospheric NO2 column；
- uncertainty/precision；
- `qa_value`；
- pixel center 与 pixel bounds；
- averaging kernel；
- tropospheric AMF；
- pressure / TM5 layer information；
- tropopause index；
- cloud fraction / cloud pressure；
- surface pressure；
- viewing/solar geometry；
- orbit/time/product processor metadata。

变量名必须在首次真实文件检查后写入**产品版本特定 schema**，禁止根据记忆硬编码。

## 4. 排放数据要求

MEIC 不只保存 total NOx。至少长期保留：
- NOx；
- VOC/NMVOC；
- CO；
- SO2；
- NH3；
- PM species（即使第一篇不用）。

sector 尽可能保持 power / industry / transport / residential / agriculture 等原始层次，以便之后设计 sector perturbation。

## 5. 地面站要求

必须分离：
- concentration table；
- station metadata；
- station relocation / validity history（如可获得）；
- timezone 和 timestamp definition。

不能只保存“城市平均值”。

## 6. 数据版本命名

推荐：

```text
{dataset_id}/{product_version}/{YYYY}/{MM}/...
```

manifest ID 示例：

```text
SAT-TROP-NO2_OFFL_processor-X_2021-2023_v001
```

任何 processor/algorithm version 跨期变化都要记录，必要时分版本处理，而不是拼在一起当同一产品。

## 7. 原始数据不可变原则

`raw/` 一经 checksum 后只读。所有裁剪、QA、重投影、垂直映射均写入 `processed/`，并携带 parent manifest ID。
