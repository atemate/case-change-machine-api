def cast_to_int_or_fail(value: float, name: str) -> int:
    if not value.is_integer():
        raise ValueError(f"{name.title()} must be integer: {value}")
    return int(value)
