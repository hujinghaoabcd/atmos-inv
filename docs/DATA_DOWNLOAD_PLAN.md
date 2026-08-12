# 数据下载与准备计划

## 1. 下载优先级

### P0 — 项目启动立即准备
1. TROPOMI NO2 L2 2021–2023；
2. ERA5 teacher episodes（先不必全三年）；
3. MEIC 2020；
4. WPS static geography；
5. CNEMC 2021–2023。

### P1 — WRF-Chem 配置冻结后
6. chemical IC/BC 对应产品；
7. domain-external anthropogenic emission；
8. biogenic/fire/dust 所需输入（根据 `chem_opt` 决定）。

### P2 — 强化论文
9. GEMS NO2；
10. Pandora/MAX-DOAS；
11. CEMS/活动 proxy。

## 2. 官方入口（启动前再次验证）

- Copernicus Data Space / Sentinel-5P: `https://dataspace.copernicus.eu/`
- Climate Data Store / ERA5: `https://cds.climate.copernicus.eu/`
- MEIC: `https://meicmodel.org.cn/`
- Copernicus Atmosphere Data Store: `https://ads.atmosphere.copernicus.eu/`
- WRF/WPS static data: `https://www2.mmm.ucar.edu/wrf/users/download/get_sources_wps_geog.html`
- GEMS/NESC: `https://nesc.nier.go.kr/`
- CNEMC: `https://www.cnemc.cn/`

接口、产品版本、认证方式可能变化，因此实际启动时必须重新核对官方文档，并更新本文件。

## 3. 下载范围

参考分析/下载 envelope：

```text
65E–145E, 10N–60N
```

这是**数据准备包络**，不是最终 WRF 投影/domain definition。

## 4. 下载程序必须具备

- resume；
- retry with backoff；
- checksum；
- request logging；
- manifest emission；
- no overwrite by default；
- product version capture；
- failed-file list；
- dry-run；
- date/orbit filtering。

## 5. TROPOMI 下载策略

按 `year/month/day` 或 orbit 分层，下载后：
1. 校验文件可打开；
2. 记录产品版本；
3. 计算 SHA256；
4. 建立 orbit/time/bbox 索引；
5. **不做永久性 QA 删除**；QA mask 在 processed stage 实现。

## 6. ERA5 下载策略

不要第一天盲目下载全部变量三年。

步骤：
1. 先冻结 WRF 输入 workflow；
2. 用 2–3 天小样本跑通 ungrib/metgrid/real；
3. 再按 episode 批量下载；
4. 若后续确需三年 neural meteorology，再另建三年 ERA5 manifest。

## 7. 下载后验收

每个 dataset 必须形成：

```text
manifest.json
checksums.sha256
inventory.csv
README.source.md
```

其中 `inventory.csv` 至少包含：文件名、时间、大小、checksum、产品版本、状态。

## 8. 禁止事项

- 不把下载 token 写入仓库；
- 不用网盘二次转载数据替代官方版本而不说明；
- 不对 raw 文件“清洗后覆盖”；
- 不把不同 processor version 静默合并；
- 不把 Level-2 只转成 GeoTIFF 后删除原文件。
