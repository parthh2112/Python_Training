


print("FIND LCM.")

def prime_factors(n):
    i = 2
    factors = []
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1
    return factors


number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))


factors1 = prime_factors(number1)
factors2 = prime_factors(number2)

all_factors = list(set(factors1 + factors2))
print(all_factors)
lcm = 1
for factor in all_factors:
    max_power = max(factors1.count(factor), factors2.count(factor))
    lcm *= factor ** max_power


print(lcm)

    
    