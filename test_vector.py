import math
from vec import Vec


def test_mean():
    v = Vec([2, 4, 6, 8])
    assert v.mean() == 5, f"Expected 5, got {v.mean()}"


def test_demean():
    v = Vec([2, 4, 6, 8])
    result = v.demean()
    assert result.elements == [-3, -1, 1, 3], f"Expected [-3, -1, 1, 3], got {result.elements}"


def test_demean_mean_is_zero():
    v = Vec([2, 4, 6, 8])
    result = v.demean()
    assert math.isclose(result.mean(), 0, abs_tol=1e-7), f"Expected ~0, got {result.mean()}"


def test_demean_does_not_change_original():
    v = Vec([2, 4, 6, 8])
    original = v.elements.copy()
    v.demean()
    assert v.elements == original, f"Expected {original}, got {v.elements}"


def test_std():
    v = Vec([2, 4, 6, 8])
    expected = 5 ** 0.5
    assert math.isclose(v.std(), expected), f"Expected {expected}, got {v.std()}"


if __name__ == "__main__":
    test_mean()
    test_demean()
    test_demean_mean_is_zero()
    test_demean_does_not_change_original()
    test_std()
    