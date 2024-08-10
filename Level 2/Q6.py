

def is_power_of_two(num):
    if num == 1:
        return True
    elif num <= 0 or num % 2 != 0:
        return False
    return is_power_of_two(num//2)


num1 = 16
num2 = 18

print(f"{num1} is a power of two:", is_power_of_two(num1))
print(f"{num2} is a power of two:", is_power_of_two(num2))  