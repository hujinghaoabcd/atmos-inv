# 计算与存储规划

本文件记录数量级和策略，不把估算值当成最终采购参数。

## 1. 外部原始数据

参考 2021–2023 全国方案：
- TROPOMI NO2 L2：数百 GB 至约 1 TB 量级；
- ERA5：取决于变量/层，约数百 GB 至 1 TB+；
- MEIC/WPS/地面站：相对较小；
- CAMS/CAM-chem：取决于提取范围；
- GEMS 全量可进一步增加 TB 级数据。

建议永久 raw storage 预留 **10 TB 量级**，实际启动前重新按产品文件做样本外推。

## 2. WRF-Chem 才是主要存储风险

全国 12 km、40 左右垂直层、小时输出，如果长期保存完整 chemistry `wrfout`，很容易进入几十 TB 甚至更高。

策略：

```text
full wrfout → temporary scratch
            → QA
            → extract selected native variables
            → build compressed teacher
            → archive manifest/restart as needed
            → delete disposable raw outputs
```

## 3. 工作空间规划

参考：
- permanent/raw：10–20 TB；
- WRF-Chem scratch：30–50 TB 更安全；
- processed teacher：数 TB 到十余 TB；
- ML runs/checkpoints：0.5–2 TB。

这些是容量级设计，不是最终精确预算。

## 4. I/O 原则

- large arrays 优先 chunked Zarr/NetCDF；
- chunking 按训练读取模式 benchmark；
- 不按“一个小时一个超小文件”形成 metadata storm；
- 不把所有 dynamic edge arrays永久复制；
- teacher/native selected 与 neural aggregated 分层保存。

## 5. Compute benchmark

正式排期前必须跑：
- 24 h WRF-Chem wall-clock benchmark；
- output GB/day；
- preprocessing GB/hour；
- neural batch throughput；
- satellite overlap throughput。

只有得到这些真实数字，才计算完整 ensemble 工期。

## 6. HPC run isolation

每个 WRF run 使用独立 run directory；输入尽量 symlink，输出写 scratch。禁止多个实验共享可修改 `namelist.input` 或 emission file。
