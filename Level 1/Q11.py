

num = 987
sum_digits = 0

while num > 0:
    sum_digits += num % 10
    num = num // 10

print(sum_digits)

