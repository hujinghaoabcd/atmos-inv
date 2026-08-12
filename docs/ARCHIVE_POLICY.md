# 数据与实验归档策略

## 永久保存

- raw external data + checksum/manifests；
- WRF-Chem run configs/manifests；
- selected native teacher variables；
- versioned teacher dataset；
- final model checkpoints；
- posterior products；
- final metrics；
- E9xx paper reproduction artifacts。

## 条件保存

- WRF restart files：保留足以恢复关键长 run 的集合；
- intermediate graph caches：重建昂贵时保存；
- debug checkpoints：项目阶段结束后清理。

## 临时 scratch

- full hourly `wrfout`（提取/QA后可删）；
- decompressed temporary satellite files；
- duplicate regridded arrays；
- failed runs。

## 删除前条件

必须存在：
1. extraction completion marker；
2. processed manifest；
3. checksum；
4. QA pass；
5. parent run manifest；
6. 必要 restart/archive policy 满足。

## Paper archive

论文提交/接收后生成 release manifest，至少包含：
- code tag；
- configs；
- data DOIs/URLs/versions；
- teacher version；
- experiment registry snapshot；
- final results checksums。
