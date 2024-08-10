

a = [1, 2, 3, 4, 5]

try:
    print(a[4])
    print(a[7])

except IndexError:
    print(f"Error: Index is out of range for list of length {len(a)}")

