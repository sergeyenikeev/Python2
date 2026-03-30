def logging(func):
 def log_function_called():
   print(f'{func} called - start.')
   func()
   print(f'{func} called - end.')
 return log_function_called

@logging
def my_name():
 print('    chris - my_name')

@logging
def friends_name():
 print('    naruto - friends_name')

friends_name()
my_name()
#=> <function my_name at 0x10fca5a60> called.
#=> chris
#=> <function friends_name at 0x10fca5f28> called.
#=> naruto