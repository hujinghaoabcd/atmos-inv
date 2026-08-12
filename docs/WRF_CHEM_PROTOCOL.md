# WRF-Chem Teacher 模拟协议

## 1. 原则

WRF-Chem 是本项目的 physics/chemistry teacher，不是真实大气的绝对真值。它有自己的物理、化学、排放和边界条件误差。因此项目需要同时：

- 学习其可用的 dynamical response；
- 用真实卫星/地面数据约束和验证；
- 防止 neural operator 只是复制 teacher bias。

## 2. 启动前必须冻结的设置

### WRF/WPS
- WRF/WPS/WRF-Chem commit/tag；
- compiler/MPI/NetCDF；
- projection/domain；
- vertical levels；
- timestep；
- microphysics；
- longwave/shortwave；
- surface layer；
- PBL；
- cumulus（12 km 是否使用需 benchmark）；
- land surface。

### Chemistry
- `chem_opt`；
- photolysis；
- aerosol option；
- biogenic emissions；
- dust/fire 是否启用；
- gas/aerosol species mapping。

### IC/BC
- meteorological IC/BC；
- chemical IC/BC；
- update interval；
- mapping table。

### Emissions
- MEIC species mapping；
- temporal profiles；
- vertical allocation；
- sector mapping；
- external-domain inventory；
- units and molecular-weight conversions。

## 3. 配置冻结流程

```text
6 h technical run
→ 24 h benchmark
→ 3–7 day episode
→ meteorology validation
→ chemistry validation
→ output/storage benchmark
→ freeze WRF-Chem protocol v1
```

在 24 h benchmark 之前不允许提交全国季节 ensemble。

## 4. Spin-up

spin-up 长度为 OPEN DECISION。应通过至少以下诊断决定：
- NO2/O3 domain mean drift；
- selected profile convergence；
- boundary influence；
- aerosol/chemical mechanism memory（若涉及）。

不要直接把“24/48/72 h”作为传统惯例照搬。

## 5. Teacher episode 选择

目标不是均匀抽日期，而是覆盖：
- shallow/deep PBL；
- strong/weak wind；
- vertical shear；
- stagnant pollution；
- frontal/transport events；
- summer photochemistry；
- winter chemistry；
- coastal/monsoon；
- basin trapping。

## 6. 输出策略

完整 `wrfout` 视为临时 scratch。长期只保存：
1. 可复现原始 run manifest；
2. 必要 restart（按项目策略）；
3. selected native vertical variables；
4. compressed teacher product；
5. diagnostics。

禁止为“以后也许有用”永久保存所有 hourly chemistry output。

## 7. Run ID

```text
W{NNNN}_{domain}_{episode}_{intervention}
```

例如：

```text
W0017_CHN12_SUMMER01_BASE
W0018_CHN12_SUMMER01_NOX125
```

每个 run 必须有不可变 manifest。

## 8. Teacher 验收

至少检查：
- simulation completeness；
- mass/unit sanity；
- meteorological error；
- surface NO2/O3；
- TROPOMI column comparison；
- profile plausibility；
- boundary artifacts；
- intervention response direction/magnitude。

只有通过质量门的 run 才进入 teacher dataset。
