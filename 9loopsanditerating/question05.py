my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for ind_list in my_list:
    for ind_values in ind_list:
        if ind_values % 2 == 0:
            print(ind_values)