def find_integers(x):
    
    integer_list = []
    
    for value in x:
        if type(value) == int:
            integer_list.append(value)
            
    return integer_list

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]


    