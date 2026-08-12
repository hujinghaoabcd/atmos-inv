# Experiment registry

`registry.csv` 是正式实验索引；`manifests/` 保存具体实验定义。

## ID ranges

- E0xx data/bootstrap
- E1xx WRF-Chem/teacher
- E2xx forward operator
- E3xx Jacobian/sensitivity
- E4xx inversion
- E5xx mechanism
- E6xx generalization
- E7xx ablation
- E8xx regional refinement
- E9xx paper reproduction

## Rule

开发 scratch 不一定要登记，但任何进入正式图表、模型选择、科学结论的 run 必须属于一个 Experiment ID。

Experiment ID 描述**问题/协议**，Run ID 描述某次实际执行；两者不能混用。
