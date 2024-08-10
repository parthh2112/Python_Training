


Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
sorted_keys = sorted(Input_list)
count = [(key, index) for index, key in enumerate(sorted_keys)]

print(count)