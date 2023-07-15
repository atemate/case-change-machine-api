def cast_to_int_or_fail(value: float | int, name: str = "value") -> int:
    if not float(value).is_integer():
        raise ValueError(f"{name.title()} must be integer: {value}")
    return int(value)
