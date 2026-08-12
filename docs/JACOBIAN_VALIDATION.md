# Jacobian / Emission-Sensitivity Validation

这是 AtmosInv 最重要的方法学质量门之一。

## 1. 为什么 RMSE 不够

用于 forward prediction 的 surrogate 只需 `C_hat` 接近 `C_teacher`；用于 inversion 的 surrogate 还需要其局部响应方向和幅度正确：

```text
J = dC / dE
```

否则 optimizer 会沿着错误梯度修改排放。

## 2. WRF-Chem reference sensitivity

使用 emission intervention finite differences：

```text
J_CTM ≈ [C(E + ΔE) - C(E)] / ΔE
```

对于非线性 regime 同时比较正/负扰动，并检查 local linearity range。

## 3. Neural sensitivity

两类：
- autograd `dC_nn/dE`；
- 用与 CTM 相同 perturbation 做 finite difference。

二者自身先应一致，否则存在实现/数值问题。

## 4. 比较对象

不仅比较 source cell：
- local response；
- downwind plume response；
- vertical profile response；
- integrated column response；
- response timing；
- regional total response。

## 5. Metrics

候选：
- correlation of sensitivity fields；
- normalized RMSE；
- cosine similarity；
- sign agreement；
- center-of-mass displacement；
- plume overlap；
- integrated response ratio；
- arrival-time error。

## 6. Acceptance gate

正式阈值需要 pilot 后冻结。规则是：

> 没有通过 Jacobian gate 的模型，即使 forward RMSE 最好，也不能进入 E400 real-satellite inversion。

必须在 experiment registry 记录 gate decision。

## 7. 关键对照

- historical-only training；
- intervention-trained；
- 2D operator；
- 3D operator；
- no-physics graph；
- physics-initialized graph。

目的：证明哪些设计真正提高 inverse reliability，而不是只提高 prediction score。
