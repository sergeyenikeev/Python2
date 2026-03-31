try:
    a = int("abc")
except ValueError as e:
    print(f"Error: {e}")