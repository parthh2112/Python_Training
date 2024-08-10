

arr = [1, 2, 3, 4, 5]
D = 2


index = len(arr) - D
arr_rotated = arr[index:] + arr[:index]

print("Original List: ",)
print("After rotation: ", arr_rotated)