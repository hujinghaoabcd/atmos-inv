# 数据质量控制（QA/QC）

## 1. 原则

QA 不应该是下载脚本里的隐藏 `if`。每个过滤条件都是版本化科学参数。

## 2. Satellite QA

记录而不是永久删除：
- qa_value；
- cloud fraction；
- snow/ice flags（如适用）；
- solar/viewing geometry；
- row/anomaly/product flags；
- retrieval uncertainty；
- surface pressure mismatch diagnostics。

至少准备 strict / reference / relaxed 三套 QA sensitivity configs。

## 3. ERA5 / meteorology QA

- missing times；
- pressure/model-level completeness；
- unit check；
- accumulated vs instantaneous variables；
- longitude convention；
- leap day/timezone/UTC。

## 4. Emission QA

- units；
- species basis（NOx as NO2-equivalent or other convention）；
- annual/monthly/hourly temporal allocation；
- sector sums；
- grid cell area；
- total national/regional mass；
- boundary overlap between MEIC and global inventory；
- no double counting。

## 5. WRF-Chem QA

每个 run 自动生成：
- missing/NaN check；
- min/max/quantiles；
- negative concentration count；
- total emission check；
- selected domain means；
- restart continuity；
- edge/boundary artifact diagnostics。

## 6. Ground observations QA

- station metadata；
- units；
- missingness；
- repeated values；
- site relocation；
- time definition；
- impossible values；
- city average only作为辅助，不替代站点验证。

## 7. QA provenance

任何 processed dataset 写入：

```text
qa_config_id
input_manifest_id
processing_git_sha
excluded_count
retained_count
reason_histogram
```
