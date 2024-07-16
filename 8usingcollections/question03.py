my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)

my_list.reverse()
my_list = my_list[1:4]
my_tuple = tuple(my_list)

print(my_tuple)
