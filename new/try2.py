try:
    # a = 10 / 0
    # a = int("abc")
    print("Hello")
except ZeroDivisionError as e:
    print(f"Error {e}")
except ValueError as e:
    print(f"Error {e}")
finally:
    print("The end.")