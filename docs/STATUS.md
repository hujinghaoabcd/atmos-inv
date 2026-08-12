# 项目状态

**Stage:** M0 — Bootstrap / Design Freeze

**Scientific production status:** NOT STARTED

当前仓库用于提前准备，尚未启动：
- 大规模数据下载；
- 全国 WRF-Chem；
- teacher ensemble；
- neural operator training；
- satellite inversion。

## 已完成准备

- 项目科学问题与创新边界；
- 全国/区域尺度参考设计；
- 数据清单与下载协议；
- WRF-Chem teacher protocol；
- emission-intervention design；
- 3D graph 与 operator architecture；
- satellite observation operator contract；
- inversion parameterization；
- Jacobian gate；
- 实验编号体系；
- 泛化/消融/机制分析方案；
- 计算存储估算；
- 风险与 fallback；
- 论文证据映射；
- startup checklist。

## 当前不应做

- 不批量下载全部数据；
- 不先拍脑袋选 `chem_opt`；
- 不开始大规模 WRF-Chem；
- 不写未经产品文档验证的 TROPOMI AK/AMF 实现；
- 不决定最终模型名字；
- 不声称任何“首次”。

## 下一次启动入口

直接执行 `STARTUP_CHECKLIST.md` 的 Phase 0–2，并更新本文件日期、负责人、计算平台和已冻结 decisions。
