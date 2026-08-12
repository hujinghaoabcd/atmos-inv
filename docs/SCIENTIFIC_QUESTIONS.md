# 科学问题、假设与可证伪设计

## Q1. 显式三维输送对卫星 NOx 排放反演有多重要？

**H1：** 在垂直风切变、深/浅边界层快速变化、复杂地形和区域输送显著的条件下，2D 或近地面输送近似会产生系统性的 emission attribution bias。

**可证伪：** 如果在严格控制模型误差后，2D 与 3D 后验排放差异主要是随机噪声，且不能由任何独立的边界层/输送变量解释，则该假设不成立。

## Q2. 这种偏差在什么大气条件下出现？

候选解释变量：
- PBLH 及其日变化；
- 垂直风切变；
- vertical velocity / turbulent mixing proxy；
- stability；
- 近地风与柱平均输送方向偏差；
- terrain relief；
- upwind emission loading；
- transport distance / residence time；
- cloud/radiation/photochemical regime。

**目标不是做相关性大拼盘**，而是形成少数有物理解释的 regime 或无量纲/标准化关系。

## Q3. 神经算子是否学到了“排放响应”，而不只是天气驱动的浓度预测？

**H2：** 只有加入 emission-intervention teacher data，模型才能在未见排放扰动上恢复合理的 `dC/dE`。

对照：
- historical-only training；
- intervention training；
- intervention + physics-informed graph。

## Q4. 神经大气算子能否跨区域泛化？

**H3：** 如果模型主要学习的是大气输送算子而非城市固定空间模板，则 leave-one-region-out 时仍应保持可接受的 forward fidelity 与 sensitivity fidelity。

## Q5. 全国共同规律是否真实存在？

不能预设“全国统一规律一定存在”。可能出现三种结果：

1. **统一规律**：相同输送指标可解释多个区域；
2. **分 regime 规律**：盆地、平原、沿海需不同机制；
3. **高度地方化**：不存在稳定跨区关系。

三种结果均可发表，只要实验能清楚区分。

## Q6. 后验排放的改善是否独立成立？

卫星拟合变好不等于排放更真实。必须考察：
- 独立地面 NO2/O3；
- 可获得的 MAX-DOAS/Pandora；
- CEMS/活动数据等排放 proxy；
- 用后验排放驱动独立 forward model 的 out-of-loop 验证。

## 研究层次

### 方法问题
- 如何构造物理初始化的 3D 动态图？
- 如何学习可微 chemistry-transport operator？
- 如何构造 native-pixel observation operator？

### 科学问题
- 2D inversion bias 是否存在？
- 在什么 regime 下存在？
- 这种 bias 是否可跨区域泛化？

论文必须让第二组问题压过第一组问题。
