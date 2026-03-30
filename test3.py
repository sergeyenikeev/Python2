gen_list = [x for x in range(10) if x % 2 == 0]

gen_list_map = list(map(lambda x: x * 2, gen_list))

print(gen_list)
print(gen_list_map)
