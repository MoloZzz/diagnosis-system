def resolve_input_value(var, val):
    if isinstance(val, str):  # Якщо "low", "medium", "high"
        mapping = {"low": 2, "medium": 5, "high": 8}
        return mapping.get(val.lower(), 5)
    elif isinstance(val, (int, float)):
        return val
    else:
        raise ValueError(f"Неприпустиме значення для {var}: {val}")
