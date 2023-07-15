import pytest
from change_machine_package.utils import cast_to_int_or_fail


@pytest.mark.parametrize("value", [1, 1.0, 0, 0.0, 100_000, 100_000.0])
def test_cast_to_int_or_fail_ok(value: int | float) -> None:
    actual = cast_to_int_or_fail(value)
    assert isinstance(actual, int)
    assert int(actual) == actual


@pytest.mark.parametrize(
    "value",
    [
        0.1,
        1e-5,
        1e-10,
    ],
)
def test_cast_to_int_or_fail_error(value: int | float) -> None:
    with pytest.raises(ValueError, match="must be integer"):
        cast_to_int_or_fail(value)
