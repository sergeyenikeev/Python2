name = 'text'
def add_chars(str1):
    print(id(str1) ) #=> 4353702856
    print( id(name) ) #=> 4353702856
  
    # новое имя, тот же объект
    str2 = str1
    print("str2 = str1")
  
    # создаем новое имя (не отличается от предыдущего) и новый объект
    print( id(str1) ) #=> 4387143328
    print(" str1 += 's'")
    str1 += 's' 
    print( id(str1) ) #=> 4387143328
    
    # объект не изменился
    print( id(str2) ) #=> 4353702856
     
add_chars(name)
print(name) #=>text
