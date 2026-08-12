"""Stable emission-correction parameterizations."""

from __future__ import annotations

import numpy as np


def apply_log_correction(prior: np.ndarray, log_alpha: np.ndarray) -> np.ndarray:
    """Return E_post = E_prior * exp(log_alpha).

    The log-space parameterization guarantees non-negative multiplicative correction
    factors without clipping. Bounds/priors belong to the inversion objective, not
    this primitive transformation.
    """
    prior_arr = np.asarray(prior, dtype=float)
    log_alpha_arr = np.asarray(log_alpha, dtype=float)
    if prior_arr.shape != log_alpha_arr.shape:
        raise ValueError("prior and log_alpha must have identical shapes")
    if np.any(prior_arr < 0):
        raise ValueError("prior emissions must be non-negative")
    return prior_arr * np.exp(log_alpha_arr)
