def add_everything_up(a, b):
    if isinstance(a, (int, float)) and isinstance(b, str):
        return str(a) + b
    elif isinstance(a, str) and isinstance(b, (int, float)):
        return a + str(b)
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return round(a + b, 3)
    return None
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))     # яблоко4215
print(add_everything_up(123.456, 7))         # 130.456