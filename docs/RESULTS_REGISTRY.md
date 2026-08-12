# 结果登记规范

正式结果应同时有机器可读 `metrics.json/parquet` 与本文件/自动报告中的摘要。

## 每个结果条目

```text
Experiment ID:
Run ID:
Git SHA:
Resolved config:
Teacher version:
Data manifests:
Seed(s):
Primary metric:
Secondary metrics:
Confidence interval:
Known failure cases:
Paper figure/table:
Decision:
```

## 结果状态

- DEV：开发结果，不可引用；
- VALIDATED：通过规定评价；
- PAPER-CANDIDATE：可进入 E9xx；
- FROZEN：最终论文证据；
- INVALIDATED：发现 bug/泄漏/版本问题，禁止引用。

如果发现错误，保留 INVALIDATED 记录而不是删除历史，说明为什么废弃。
