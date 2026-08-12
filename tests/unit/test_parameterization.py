import numpy as np
import pytest

from atmos_inv.inversion.parameterization import apply_log_correction


def test_zero_log_correction_preserves_prior() -> None:
    prior = np.array([1.0, 2.0, 0.0])
    result = apply_log_correction(prior, np.zeros_like(prior))
    np.testing.assert_allclose(result, prior)


def test_log_correction_is_positive() -> None:
    prior = np.array([1.0, 2.0])
    result = apply_log_correction(prior, np.log(np.array([0.5, 1.5])))
    np.testing.assert_allclose(result, np.array([0.5, 3.0]))


def test_negative_prior_rejected() -> None:
    with pytest.raises(ValueError):
        apply_log_correction(np.array([-1.0]), np.array([0.0]))
