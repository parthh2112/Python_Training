


arr = [1, 2, 3, 4, 5]
k = 6
pair_count = 0
num_count = {}

for num in arr:
    complement = k - num
    if complement in num_count:
        pair_count += num_count[complement]
    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 1

print("Total Pairs: ", pair_count)



        
       