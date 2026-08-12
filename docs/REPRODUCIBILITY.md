# 可复现性与科研证据链

## 1. 最终目标

论文中的任意数值能够追溯：

```text
figure/table cell
→ experiment_id
→ run_id
→ resolved config
→ Git SHA
→ model checkpoint
→ teacher version
→ WRF run IDs
→ raw data manifests/checksums
```

## 2. Git 管什么

提交：
- code；
- configs；
- manifests（不含秘密）；
- docs；
- tests；
- experiment registry；
- small metadata/results summaries。

不提交：
- raw atmospheric data；
- wrfout；
- huge checkpoints；
- secrets/token；
- temporary plots。

## 3. Resolved config

Hydra 多层配置组合后，**最终 resolved config 必须复制到 run directory**。只保存命令行参数不够。

## 4. Randomness

神经实验：
- 明确 seed；
- 正式结果多个 seed；
- 记录 CUDA/cuDNN deterministic choices；
- 不承诺不同 GPU/版本 bitwise identical，报告允许的数值差异。

## 5. 数据 manifest

每个 processed dataset 记录：
- parent manifest；
- code Git SHA；
- config hash；
- creation timestamp；
- file inventory/checksum；
- QA criteria；
- split manifest。

## 6. Experiment registry

`experiments/registry.csv` 是论文实验入口。正式 run 不允许只有 MLflow ID 而没有 Experiment ID。

## 7. Paper reproduction

提交前创建冻结 tag，例如：

```text
paper-v1-submission
```

执行 E9xx，从空 results 目录重建：
- main tables；
- main figures；
- supplement metrics；
- provenance report。

## 8. Environment

Python 环境和 WRF-Chem compiled stack 分开记录。WRF run manifest 必须包含 compiler/MPI/NetCDF/HDF5/WRF commit；ML run 记录 Python/PyTorch/CUDA/PyG。
