try:
    x = int("abc")
except ValueError as e:
    print(f"Ошибка ValueError occurred: {e}")
    