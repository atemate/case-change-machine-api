def cast_to_int_or_fail(value: float | int, name: str = "value") -> int:
    value = float(value)
    value = round(value, 12)  # fix: 4.9 * 100 = 490.00000000000006
    if not value.is_integer():
        raise ValueError(f"{name} must be integer: {value}")
    return int(value)
