try:
    # a = 10 / 0
    # a = int("abc")
    print("Hello")
    # raise Exception("Моя ошибка")
except ZeroDivisionError as e:
    print(f"Error {e}")
except ValueError as e:
    print(f"Error {e}")
except BaseException as e:
    print(f"Ошибка: {e}")
else:
    print("else")
finally:
    print("The end.")