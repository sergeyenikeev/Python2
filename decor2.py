def log1(func):
    def log1_function_called():
        print("decor begin")
        func()
        print("decor end")
    return log1_function_called

@log1
def my_function():
    print("  my_function")

my_function()
